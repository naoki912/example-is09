# https://editor.ponyorm.com/user/naoki912/is09/python

from datetime import datetime
from pony.orm import *


db = Database()


class GiftCode(db.Entity):
    _table_ = 'gift_code'
    id = PrimaryKey(int, auto=True)
    code = Optional(str, 16, unique=True)
    balance = Optional(int)
    expiration_date = Optional(datetime)
    updated_date = Optional(datetime, default=lambda: datetime.now(), volatile=True)
    settlement = Optional('Settlement')


class Product(db.Entity):
    _resource_ = 'product'
    id = PrimaryKey(int, auto=True)
    name = Optional(str, 255)
    price = Optional(int)
    overview = Optional(str, 255)
    created_date = Optional(datetime, default=lambda: datetime.now())
    updated_date = Optional(datetime, default=lambda: datetime.now(), volatile=True)
    transitions = Set('Transition')
    url = Optional(str)


class Settlement(db.Entity):
    _table_ = 'settlement'
    id = PrimaryKey(int, auto=True)
    gift_code_id = Required(GiftCode)
    created_date = Optional(datetime, default=lambda: datetime.now())
    updated_date = Optional(datetime, default=lambda: datetime.now(), volatile=True)
    transitions = Set('Transition')


class Transition(db.Entity):
    _table_ = 'transitions'
    id = PrimaryKey(int, auto=True)
    price = Optional(int)
    created_date = Optional(datetime, default=lambda: datetime.now())
    updated_date = Optional(datetime, default=lambda: datetime.now(), volatile=True)
    settlement = Required(Settlement)
    product = Required(Product)
