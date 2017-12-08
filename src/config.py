class Config(object):
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    # gift code作成時のデフォルト残高
    DEFAULT_BALANCE = 5000


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:password@127.0.0.1/db"
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
