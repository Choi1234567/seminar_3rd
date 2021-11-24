import time
import timeit


def profile(f):
    def calculate_execution_time(*args, **kwargs):
        start = timeit.default_timer()
        res = f(*args, **kwargs)
        print("the execution time of function ", f.__name__, " is ", (timeit.default_timer() - start) * 1000, " ms")
        return res

    return calculate_execution_time


@profile
def some_function():
    return sum(range(10000))


def operate():
    print('===in operation===')


class timer:
    start = 0

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("the execution time of this statement  is ", (timeit.default_timer() - self.start) * 1000, " ms")
        return self


result = some_function()

with timer():
    print(sum(range(1000)))
