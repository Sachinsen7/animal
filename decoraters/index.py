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



# dubugging function calls


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        # reverse loop
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)    
    return wrapper

@debug
def hello():
    print("good morning")


@debug
def greeting(name, greeting = "Hello"):
    print(f"{greeting}, {name}")


hello()
greeting("Sachin", greeting="Hey")



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