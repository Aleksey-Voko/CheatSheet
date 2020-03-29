"""Создадим исключение, которое называется UppercaseException,
и вызовем его, когда встретим слово, записанное в верхнем регистре."""


class UppercaseException(Exception):
    pass


words = ['eeenie', 'meenie', 'miny', 'MO']

for word in words:
    if word.isupper():
        raise UppercaseException(word)

# Traceback (most recent call last):
#   File "G:/Tools/Py/Project/Lessons/Training/tmpl.py", line 13, in <module>
#     raise UppercaseException(word)
# __main__.UppercaseException: MO
