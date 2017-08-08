# coding: utf-8
import os


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = "0.0.0.0"
    PORT = 5000
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:qwerty12345@db:5432/spiner_db"
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = './media'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    BLUEPRINTS = [
        'spiner.spiner',
    ]


class DevelopConfig(BaseConfig):
    DEBUG = True
