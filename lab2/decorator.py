import time

class Decorator:

    def __init__(self, func):
        self.history = []
        self.func = func

    def history_update(self, func_name, call_time, *args):
        tm = time.strftime("%H:%M:%S", call_time)
        self.history.append(f"<{tm}> : function {func_name} called with arguments{[arg for arg in args]}")


class PerfomanceDecorator(Decorator):

    def print_time(self, tm):
        print("\t", format(self.time, '.9f'))

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

class HTMLDecorator(Decorator):

    def __call__(self, *args, **kwargs):
        print("<html>\n\t<body>")
        res = self.func(*args, **kwargs)
        print("\t</body>\n</html>")
        self.history_update(self.func.__name__, time.localtime(), *args, **kwargs)


@HTMLDecorator
@PerfomanceDecorator
def quad_1(nums):
    quads = []

    for num in nums:
        quads.append(num*num)
    return quads

@HTMLDecorator
@PerfomanceDecorator
def quad_2(nums):
   quads = [num*num for num in nums]
   return quads

@HTMLDecorator
@PerfomanceDecorator
def quad_3(nums):
    return map(lambda x: x*x, nums)


nums = [1, 2, 3, 4, 5, 6]

print('Loop:')
quad_1(nums)
print('List comprehension:')
quad_2(nums)
print('Map:')
quad_3(nums)
