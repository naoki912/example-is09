from functools import wraps

from flask import request

from model.gift_code import GiftCode


class AuthenticationError(Exception):
    def __init__(self, message):
        self.message = message


def auth(f):
    """
    なんちゃってauth実装
    これをResourceのget()とかput()とかの前に書けばおｋ

    Example:
        >> @auth
        >> def get():
        >>     ...
        >>
        >> @auth
        >> def post():

    もし認証方法を変えたかったらwrapper()の中身を変更してください

    :param f:
    :return:
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Token', None)
        if token is None:
            raise AuthenticationError('Token not found')

        gift_code = GiftCode.query.filter_by(code=token).first()
        if gift_code is None:
            raise AuthenticationError('Invalid token')

        return f(*args, **kwargs)
    return wrapper
