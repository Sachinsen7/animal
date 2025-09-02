mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple = ("Max", 28, "Boston")
my = ("Max,")
print(type(mytuple))

mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

mytuple = tuple(["Max", 28, "Boston"])
item = mytuple[2]
print(item)

mytuple = tuple(["Max", 28, "Boston"])
for i in mytuple:
    print(i)

mytuple = tuple(["Max", 28, "Boston"])
if "Max" in mytuple:
    print("Yes")
else:
    print("No")

my_tuple = ('a', 'p', 'b', 'l', 'e')
print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index('e'))

my_tuple = ('a', 'p', 'b', 'l', 'e')
mylist = list(my_tuple)
print(mylist)
my_tuple2 = tuple(my_tuple)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:]#[:5] [2:] [2::] [::2] ::1 ::-1
print(b)

my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = [0, 1, 2, "hello", True]

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")


import timeit
print(timeit.timeit(stmt= "[0, 1, 2, 3, 4, 5]", number = 1000000))
print(timeit.timeit(stmt= "[0, 1, 2, 3, 4, 5]", number = 1000000))

