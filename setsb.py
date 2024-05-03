#unordered, mutable no duplicates

myset = {1, 2, 3}
print(myset)

myset = {1, 2, 3, 1, 3}
print(myset)

myset = ([1, 2, 3])
print(myset)

myset = set("Hello")
print(myset)

myset = {}
print(type(myset))

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(4)
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.clear()
print(myset)

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

myset.pop()
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

for i in myset:
    print(i)

if 1 in myset:
    print("Yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)
i = odds.intersection(primes)
print(i)
i = evens.intersection(odds)
print(i)


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB)
print(diff)
diff = setB.difference(setA)
print(diff)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
print(setB.symmetric_difference(setA))

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setB)

setA.difference_update(setB)
print(setB)

setA.symmetric_difference_update(setB)
print(setB)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB))
print(setB.issubset(setA))

print(setB.issuperset(setA))
print(setA.issuperset(setB))

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.isdisjoint(setC))

setA = {1, 2, 3, 4, 5}
setA = setB
setB.add(7)
print(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = set(setA)  #setB = setA.copy()
setB.add(7)
print(setB)
print(setA)

a = frozenset([1, 2, 3, 4])
print(a)           #it cannot and and remove

