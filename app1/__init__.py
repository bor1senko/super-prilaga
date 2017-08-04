from flask import Blueprint

app1 = Blueprint(
    'app1', __name__,
    template_folder='templates',
    url_prefix='/api/v1/'
)

from view import *