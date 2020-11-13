class Tracer(object):
    """
    Считает количество вызовов декорируемой функции.
    Можно декорировать и функции и методы классов.
    """

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return wrapper


if __name__ == '__main__':
    @Tracer
    def spam(a, b, c):
        print(a + b + c)


    @Tracer
    def eggs(N):
        return 2 ** N


    spam(1, 2, 3)
    spam(a=4, b=5, c=6)
    print(eggs(32))


    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @Tracer
        def give_raise(self, percent):
            self.pay *= (1.0 + percent)

        @Tracer
        def last_name(self):
            return self.name.split()[-1]


    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.give_raise(.10)
    print(int(sue.pay))
    print(bob.last_name(), sue.last_name())
