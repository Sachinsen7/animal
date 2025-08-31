def function(x):
    def inner_function(y):
        return x + y
    return inner_function

function(2)(3)


def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

outer()