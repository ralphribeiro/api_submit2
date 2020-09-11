from os import environ

from flask import Flask
from flask.cli import with_appcontext
import click
from flask.globals import current_app
from flask_migrate import Migrate

from app.resources import configure as config_db


@click.command()
@with_appcontext
def config():
    from pprint import pprint
    pprint(current_app.config)


def create_app(nome_config=environ.get('FLASK_ENV')):
    app = Flask(__name__)

    app.config.from_object(f'config.{nome_config}')
    config_db(app)
    migrate = Migrate(app, app.db)
    app.cli.add_command(config)

    from app.api import api
    app.register_blueprint(api)

    return app
