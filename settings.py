# coding: utf-8
import os


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:qwerty12345@localhost/spiner_db"
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = './media'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    BLUEPRINTS = [
        'app1.app1',
    ]


class DevelopConfig(BaseConfig):
    DEBUG = True
