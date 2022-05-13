from flask import redirect, render_template, url_for

from bookface.manage_users import admin
from bookface.manage_users.services.manage_users_service import ManageUsersService
from bookface.auth.services.user_service import UserService
from bookface import db


@admin.route('/')
def admin_panel():
    users = ManageUsersService().get_all_users()
    return render_template("admin_panel.html", users = users)

@admin.route('/block/<user_id>')
def block(user_id):
        user_to_block = UserService().get_by_id(user_id)
        user_to_block.role_id=4
        UserService().flush()
        return redirect(url_for('admin.admin_panel'))


@admin.route('/unblock/<user_id>')
def unblock(user_id):
    user_to_unblock = UserService().get_by_id(user_id)
    user_to_unblock.role_id = 3
    UserService().flush()
    return redirect(url_for('admin.admin_panel'))



