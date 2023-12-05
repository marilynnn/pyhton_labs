import time

class Decorator:

    def __init__(self, func):
        self.history = []
        self.func = func

    def history_update(self, func_name, call_time, *args):
        tm = time.strftime("%H:%M:%S", call_time)
        self.history.append(f"<{tm}> : function {func_name} called with arguments{ [arg for arg in args]}")


class DecoratorFirst(Decorator):

    def print_time(self, tm):
        print(format(self.time, '.9f'))

    @property
    def __name__(self):
        return self.func.__name__

    def __call__(self, *args, **kwargs):
        time1 = time.perf_counter()
        res = self.func(*args, **kwargs)
        time2 = time.perf_counter()
        self.time = time2 - time1
        self.print_time(self.time)
        self.history_update(self.func.__name__, time.localtime(), *args, **kwargs)
        return res

class DecoratorSecond(Decorator):

    def print_time(self):
        print(f"<html><body>{self.func.time:.10f}</body></html>")

    def __call__(self, *args, **kwargs):
        res = self.func(*args, **kwargs)
        self.history_update(self.func.__name__, time.localtime(), *args, **kwargs)
        self.print_time()


@DecoratorSecond
@DecoratorFirst
def quad_1(nums):
    quads = []

    for num in nums:
        quads.append(num*num)
    return quads

@DecoratorSecond
@DecoratorFirst
def quad_2(nums):
   quads = [num*num for num in nums]
   return quads

@DecoratorSecond
@DecoratorFirst
def quad_3(nums):
    return map(lambda x: x*x, nums)


nums = [1, 2, 3, 4, 5, 6]

print('Loop:')
quad_1(nums)
print('List comprehension:')
quad_2(nums)
print('Map:')
quad_3(nums)
