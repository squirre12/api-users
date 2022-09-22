import pathlib
from environs import Env

BASE_DIR = pathlib.Path(__file__).parent

env = Env()
env.read_env()

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")


class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
