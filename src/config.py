class Config(object):
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = False
    DB = {
        'TYPE': 'sqlite',
        'NAME': 'db.sqlite3'
    }
    # gift code作成時のデフォルト残高
    DEFAULT_BALANCE = 5000
