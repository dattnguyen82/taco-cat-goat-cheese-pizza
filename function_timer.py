from time import time


def function_timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        elapsed = t2 - t1
        return result, elapsed
    return wrap_func
