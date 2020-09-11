from os.path import abspath, dirname


class Config():
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{abspath(dirname(__file__))}/submit.db'

class development(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class testes(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class production(Config):
    DEBUG = False