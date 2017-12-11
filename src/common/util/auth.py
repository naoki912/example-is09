from functools import wraps

from flask import request

from model.gift_code import GiftCode


class AuthenticationError(Exception):
    def __init__(self, message):
        self.message = message


def auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.form.get('token', None)
        if token is None:
            raise AuthenticationError('Token not found')

        gift_code = GiftCode.query.filter_by(code=token).first()
        if gift_code is None:
            raise AuthenticationError('Invalid token')

        return f(*args, **kwargs)
    return wrapper
