from flask import Flask

from app.config import Config
from app.extensions import db
from app.views import static_blueprint, home_blueprint, submit_blueprint
from app.commands import init_db


BLUEPRINTS = [
    static_blueprint,
    home_blueprint,
    submit_blueprint
]

COMMANDS = [
    init_db, 
]

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    register_extension(app)
    register_blueprints(app)
    register_commands(app)

    return app

def register_extension(app):
    db.init_app(app)

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)