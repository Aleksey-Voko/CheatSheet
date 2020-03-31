import inspect
import string


def is_str(val):
    return isinstance(val, str)


for name, value in inspect.getmembers(string, is_str):
    if not name.startswith('_'):
        print(f"{name}={bytes(value, encoding='utf-8')}")


# ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits='0123456789'
# hexdigits='0123456789abcdefABCDEF'
# octdigits='01234567'
# printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# whitespace=' \t\n\r\x0b\x0c'
