mylist = ["Banana", "Cherry", "Apple"]

mylist2 = [5, True, "Apple", "Apple"]
mylist2 = list()
print(mylist2)

item = mylist[0]
print(item)

for i in mylist:
    print(i)

if "Banana" in mylist:                      #Lemon
    print("Yes")
else: print("No")

mylist = ["Banana", "Cherry", "Apple"]
print(len(mylist))             #Total count

mylist = ["Banana", "Cherry", "Apple"]
mylist.append("lemon")
print(mylist)

mylist = ["Banana", "Cherry", "Apple"]
mylist.insert(1, "Blackberry")
print(mylist)

mylist = ["Banana", "Cherry", "Apple"]   #delete the last variable
item = mylist.pop()
print(mylist)

mylist = ["Banana", "Cherry", "Apple"]
item = mylist.remove("Cherry")
print(mylist)

mylist = ["Banana", "Cherry", "Apple"]
item = mylist.clear()
print(mylist)

mylist = ["Banana", "Cherry", "Apple"]
item = mylist.reverse()
print(mylist)

mylist = ["Banana", "Cherry", "Apple"]
item = mylist.sort()                           #Alphabetical order
print(mylist)

mylist = [4, -5, 3, -1, 0, 2, 3, 5]
item = mylist.sort()
new_list = sorted(mylist)
print(mylist)
print(new_list)

mylist = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

a = mylist[::2] #[1:5] [:1] [1:] [2::]
print(a)

list_org = ["Banana", "Cherry", "Apple"]
list_cpy = list_org
print(list_cpy)

list_org = ["Banana", "Cherry", "Apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

list_org = ["Banana", "Cherry", "Apple"]
list_cpy = list_org.copy()
print(list_cpy)

list_org = ["Banana", "Cherry", "Apple"]
list_cpy = list(list_org)

print(list_org)

mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]

print(mylist)
print(b)

