import click
from flask.cli import with_appcontext

from app.extensions import db

@click.command('init_db')
@with_appcontext
def init_db():
    click.echo('Database creation in progress')
    
    db.drop_all()
    db.create_all()

    click.echo('Database was created')