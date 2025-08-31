#Dictionary is collection data type that is unordered and mutable. it consists of collection of key value pairs
myDict = {"name":"Max", "age":"28,", "city":"New York"}
print(myDict)

myDict2 = dict(name="Mary", age=27, city="Boston")
print(myDict2)

value = myDict["name"]
print(value)

myDict["email"] = "max@xyz.com"
print(myDict)

myDict["email"] = "coolmax@xyz.com"
print(myDict)

mydict = {"name":"Max", "age":"28,", "city":"New York"}
del mydict["name"]
print(mydict)

mydict = {"name":"Max", "age":"28,", "city":"New York"}
mydict.pop("age")
print(mydict)

mydict = {"name":"Max", "age":"28,", "city":"New York"}
mydict.popitem()
print(mydict)

mydict = {"name":"Max", "age":"28,", "city":"New York"}
if "name" in mydict:
    print(mydict["name"])

mydict = {"name":"Max", "age":"28,", "city":"New York"}
try:
    print(mydict["name"])
except:
    print("Error")

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for values in mydict.values():
    print(values)

for key, value in mydict.items():
    print(key, value)

mydict_cpy = mydict

mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

my_dict = {"name":"Max", "age":"28,", "email":"max@xyz"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")

mydict.update(my_dict_2)
print(my_dict_2)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

mytuple = (8, 7)
my_dict = {mytuple: 15}
print(my_dict)