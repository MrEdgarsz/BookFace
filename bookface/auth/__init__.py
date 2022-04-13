from flask import Blueprint, render_template

from bookface.auth.controllers.login_controller import sign_in

auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder="pages")
