def square(number):
    return number ** 2

result = square(5)
print(result)



# multiple parameters

def add_two_num(num_one, num_two):
    return num_one + num_two

print(add_two_num)


#  multiply

def multiply(p1, p2):
    return p1 * p2

print(multiply(4, 5))
print(multiply('a', 5))
print(multiply(5, "a"))


#  returning mutliple values

import math

def circle_stats(radius):
    area = math.floor(math.pi * radius ** 2)
    circumference = math.floor(2 * math.pi * radius)
    return area, circumference

area, circumference = circle_stats(3)
print("area: ", area, "circumference: ", circumference)



#  greet a user


def greet(name = "user"):
    return "Hello, " + name + " !"

print(greet("Sachin"))


#  lambda function | anonymous function

def add(a, b):
 return a + b

result = add(1, 2)

# #######################

cube = lambda x: x ** 3

print(cube)


#  function with arguments 

def sum_all(*args):
 
 return sum(args)


# print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5, 6, 7))


# funcgion with multiple arguments

def print_all(**kwargs):
    for key, value in kwargs.items():
       print(f"{key}: {value}")


print_all(name="shaktiman", power="lazer")
print_all(name="Ironman", power="lazerbeam")
print_all(name="spidermane", power="web shoot", real_name="peter parker")


# generator function with yield

def even_generator(limit):
   for i in range(2, limit + 1, 2):
      yield i

print(even_generator(10)) # not work

# yield => generater

for num in even_generator(10):
   print(num)



#  recursive number
# factorial number

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

