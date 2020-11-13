import time


class Timer:
    def __init__(self, func):
        self.func = func
        self.all_time = 0

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        delta_time = time.time() - start
        self.all_time += delta_time
        print(f'{self.func.__name__}: delta_time = {delta_time:.5f}, all_time = {self.all_time:.5f}')
        return result


if __name__ == '__main__':
    @Timer
    def list_comp(count):
        return [x * 2 for x in range(count)]

    @Timer
    def map_call(count):
        return list(map(lambda x: x * 2, range(count)))


    list_comp(500000)
    list_comp(5000000)
    list_comp(10000000)
    print(f'all_time = {list_comp.all_time}')

    print('=' * 51)

    map_call(500000)
    map_call(5000000)
    map_call(10000000)
    print(f'all_time = {map_call.all_time}')

    print('=' * 51)


# Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40)
# [MSC v.1927 64 bit (AMD64)] on win32
# ---------------------------------------------------
# list_comp: delta_time = 0.03900, all_time = 0.03900
# list_comp: delta_time = 0.41544, all_time = 0.45444
# list_comp: delta_time = 0.84288, all_time = 1.29733
# all_time = 1.2973253726959229
# ===================================================
# map_call: delta_time = 0.07300, all_time = 0.07300
# map_call: delta_time = 0.74600, all_time = 0.81900
# map_call: delta_time = 1.51803, all_time = 2.33703
# all_time = 2.3370254039764404
# ===================================================
#
# Python 3.6.9 (2ad108f17bdb, Apr 07 2020, 03:05:35)
# [PyPy 7.3.1 with MSC v.1912 32 bit] on win32
# ---------------------------------------------------
# list_comp: delta_time = 0.00399, all_time = 0.00399
# list_comp: delta_time = 0.02400, all_time = 0.02799
# list_comp: delta_time = 0.04800, all_time = 0.07600
# all_time = 0.07599616050720215
# ===================================================
# map_call: delta_time = 0.01800, all_time = 0.01800
# map_call: delta_time = 0.14700, all_time = 0.16500
# map_call: delta_time = 0.28699, all_time = 0.45200
# all_time = 0.4519970417022705
# ===================================================
