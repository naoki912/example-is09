from random import choice
from string import ascii_letters
from string import digits


def generate_code(size=16, chars=ascii_letters + digits):
    return ''.join(choice(chars) for _ in range(size))
