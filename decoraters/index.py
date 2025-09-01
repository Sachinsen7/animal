#  Timing function execution 
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def exa_func(n):
    return time.sleep(n)

exa_func(3)





#  cache return value => most used

def cache(func):
    cache_value = {}  # dictionary is easy to access
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def example_func(a, b):
    time.sleep(4)
    return a + b

example_func(3, 6)
example_func(3, 6)