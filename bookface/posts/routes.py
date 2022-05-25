from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from datetime import datetime
from time import strftime

from bookface import db
from bookface.manage_users.services.manage_users_service import ManageUsersService
from bookface.posts import postboard
from bookface.posts.models.post import Post
from bookface.posts.services.post_service import PostService
from bookface.posts.forms.post_form import PostForm

from bookface.auth.services.user_service import UserService
from bookface.auth.models.user import User

@postboard.route("/", methods=["GET", "POST"])
@login_required
def postboard_page():
    posts = PostService().get_all_by_created_at()
    form = PostForm()

    if form.validate_on_submit():
        post_to_create = Post(description=form.content.data, user_id=current_user.id)
        PostService().create(post_to_create)
        PostService().flush()
        flash("Pomyślnie opublikowano twój post", category="success")
        return redirect(url_for('postboard.postboard_page'))

    if form.errors != {}:
        for error in form.errors.values():
            flash(f"Wystąpił błąd podczas publikacji twojego posta: {error}", category="danger")

    return render_template("postboard.html", posts=posts, form=form)

@postboard.route("/edit/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = PostService().get_by_id(post_id)

    if request.method == "POST":
        post_to_edit.description = request.form['content']  
        post_to_edit.updated_at = datetime.now()   

    PostService().flush()
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/delete/<post_id>")
def delete_post(post_id):
    post_to_delete = PostService().get_by_id(post_id)
    PostService().delete(post_to_delete)
    PostService().flush()
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/block_user/<user_id>")
def block_user(user_id):
    ManageUsersService().ban_user(user_id)
    ManageUsersService().flush()
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/unblock_user/<user_id>")
def unblock_user(user_id):
    ManageUsersService().unban_user(user_id)
    ManageUsersService().flush()
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/like/<post_id>")
def like_post(post_id):
    post_to_update = PostService().get_by_id(post_id)
    post_to_update.likes += 1
    # post_to_update.likers.append(current_user)
    PostService().flush() 
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/unlike/<post_id>")
def unlike_post(post_id):
    post_to_update = PostService().get_by_id(post_id)

    if post_to_update.likes > 0:
        post_to_update.likes -= 1
        # post_to_update.likers.remove(current_user)
        PostService().flush()

    return redirect(url_for('postboard.postboard_page')) 