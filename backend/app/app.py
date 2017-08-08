from flask import Flask
from flask import render_template
from settings import DevelopConfig

import importlib


class AppFactory(object):
    def __init__(self, config=None):
        self.app_config = config

    def get_app(self, app_name, **kwargs):
        self.app = Flask(app_name, **kwargs)
        if self.app_config:
            self.app.config.from_object(self.app_config)

        self._register_db()
        self._register_blueprints()
        return self.app

    def _register_blueprints(self):
        for path in self.app.config.get("BLUEPRINTS", []):
            module_name, blueprint_name = path.split('.')
            module = importlib.import_module(module_name)
            self.app.register_blueprint(getattr(module, blueprint_name))

    def _register_db(self):
        import ext
        if hasattr(ext, 'db'):
            ext.db.init_app(self.app)


app = AppFactory(DevelopConfig).get_app(__name__)


@app.route('/')
def index():
    return render_template('index.html')
