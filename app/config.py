from os import path, sep, pardir

class Config:
    SECRET_KEY = "7Bn5P2wN9LkR3zQmYsXu8cHvA4bE6gF1TJiGyDx"
    BASE_DIR = path.abspath(path.dirname(__file__) + sep + pardir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'database.db')