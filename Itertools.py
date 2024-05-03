#Itertools: Product, permutations, Combinations, accumulate. groupby, and infinite intertools
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

a = [1, 2]
b = [3]
prod = product(a, b, repeat = 2)
print(list(prod))


from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2)
print(list(perm))

from itertools import combinations
a = [1, 2, 3, 4]
Comb = combinations(a, 2)
print(list(Comb))

from itertools import combinations_with_replacement
a = [1, 2, 3, 4]
Comb_wr = combinations_with_replacement(a, 2)
print(list(Comb_wr))

from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))    #sum of each other

from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))  #multiply of each other


import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))

from itertools import groupby
def smaller_than_3(x):
    return x< 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)  #try lambda x: x<3 it will do the same thing
for key, value in group_obj:
    print(key, list(value))

from itertools import groupby
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Aman', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Shubham', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))


from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3, 4]
for i in cycle(a):
    print(i)
    break

a = [1, 2, 3]
for i in repeat(1, 4):
    print(i)
