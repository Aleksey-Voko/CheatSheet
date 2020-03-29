def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


def double_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return new_function


@double_it
@square_it
@document_it
def add_inst(a, b):
    return a + b


print(add_inst(5, b=7))
