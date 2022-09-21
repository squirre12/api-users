import pathlib

BASE_DIR = pathlib.Path(__file__).parent

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://itvdn:itvdn@localhost:5432/user_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False