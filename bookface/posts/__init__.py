from flask import Blueprint

postboard = Blueprint('postboard', __name__, url_prefix='/postboard', template_folder="pages")