from random import choice

from .string import ascii_string_for_gift_code


def generate_code(size=16, chars=ascii_string_for_gift_code):
    """
    ギフトコードの `コード` を生成する。

    デフォルトでは「0(ゼロ)」と「O(オー)」などの、
    フォントによっては判別がしにくい文字を除いた文字列から
    16文字のコードを生成する

    :param size:
    :param chars:
    :return:
    """

    return ''.join(choice(chars) for _ in range(size))
