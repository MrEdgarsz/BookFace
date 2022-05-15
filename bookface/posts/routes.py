from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from datetime import datetime
from time import strftime

from bookface import db
from bookface.posts import postboard
from bookface.posts.models.post import Post
from bookface.posts.services.post_service import PostService
from bookface.posts.forms.post_form import PostForm

from bookface.auth.services.user_service import UserService
from bookface.auth.models.user import User

@postboard.route("/", methods=["GET", "POST"])
def postboard_page():
    posts = PostService().get_all_by_created_at()
    form = PostForm()

    if form.validate_on_submit():
        post_to_create = Post(description=form.content.data, user_id=1)
        PostService().create(post_to_create)
        PostService().flush()
        flash("Pomyślnie dodano twój post na tablicę", category="success")
        return redirect(url_for('postboard.postboard_page'))

    if form.errors != {}:
        for error in form.errors.values():
            flash(f"Wystąpił błąd podczas dodawania twojego posta na tablicę: {error}", category="danger")

    return render_template("postboard.html", posts=posts, form=form)

@postboard.route("/delete_post/<post_id>")
def delete_post(post_id):
    post_to_delete = PostService().get_by_id(post_id)
    PostService().delete(post_to_delete)
    PostService().flush()
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/update_post/<post_id>", methods=["GET", "POST"])
def update_post(post_id):
    post_to_update = PostService().get_by_id(post_id)

    if request.method == "POST":
        post_to_update.description = request.form['content']  
        post_to_update.updated_at = datetime.now()   

    PostService().flush()
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/send_like/<post_id>", methods=["GET", "POST"])
def send_like(post_id):
    post_to_update = PostService().get_by_id(post_id)
    post_to_update.likes += 1
    PostService().flush() 
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/block_user/<user_id>")
def block_user(user_id):
    user_to_block = UserService().get_by_id(user_id)
    user_to_block.role_id = 4
    UserService().flush() 
    return redirect(url_for('postboard.postboard_page')) 

@postboard.route("/unblock_user/<user_id>")
def unblock_user(user_id):
    user_to_unblock = UserService().get_by_id(user_id)
    user_to_unblock.role_id = 3
    UserService().flush()
    return redirect(url_for('postboard.postboard_page')) 