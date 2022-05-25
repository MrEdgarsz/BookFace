from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from bookface.manage_users import admin
from bookface.manage_users.services.manage_users_service import ManageUsersService
from bookface import db

@admin.route('/')
@login_required
def admin_panel():
    users = ManageUsersService().get_all_users()
    if current_user.role_id!=1:
        return redirect(url_for("postboard.postboard_page"))
    return render_template("admin_panel.html", users=users)

@admin.route('/block/<user_id>')
def block(user_id):
        ManageUsersService().ban_user(user_id)
        ManageUsersService().flush()
        return redirect(url_for('admin.admin_panel'))


@admin.route('/unblock/<user_id>')
def unblock(user_id):
    ManageUsersService().unban_user(user_id)
    ManageUsersService().flush()
    return redirect(url_for('admin.admin_panel'))



