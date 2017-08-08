from flask import Blueprint

spiner = Blueprint(
    'spiner', __name__,
    template_folder='templates',
    url_prefix='/api/v1/'
)

from view import *
