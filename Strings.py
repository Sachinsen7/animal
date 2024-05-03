my_string = 'Hello World' #You can also use ""
print(my_string)

my_string = 'I\'m a programmer' #You can also use "" double qoute
print(my_string)

my_string = """Hello
world"""
print(my_string)

my_string = "Hello World"
char = my_string[0]#1, 2, 3,
print(char)

my_string = "Hello World"
substring = my_string[::-1] #
print(substring)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

greeting = "Hello"
for i in greeting:
    print(i)

greeting = "Hello"
if 'e' in greeting:
    print("Yes")
else:
    print("No")

my_string = '  hello world  '
my_string = my_string.strip()
print(my_string)

my_string = "Hello World!"
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("Hello")) #put anything etc.
print(my_string.endswith("World"))

print(my_string.find('o'))
print(my_string.count('H'))
print(my_string.replace('World', 'Universe'))

my_string = 'How are you doing'
my_list = my_string.split(" ")
print(my_list)

my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)


my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)
new_string = ''.join(my_list)
print(my_string)


my_list = ['a'] * 6 # Try 1000000
print(my_list)

#Bad

my_string = ''
for i in my_list:
    my_string += i
print(my_string)



#Good

my_string = ''.join(my_list)
print(my_string)

from timeit import default_timer as timer

my_list = ['a'] * 100000


#bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)

#Good

start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start)


# %, format(), fstrings

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
print(my_string)

var = 3.1234567
my_string = "the variable is %.2f" % var
print(my_string)

#Format method

var = 3.1234567
var2 = 6
my_string = "the variable is {}".format(var)
print(my_string)

my_string = "the variable is {:.2f}".format(var)
print(my_string)

var = 3.1234567
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)

my_string = f" the variable is {var} and {var2}"
print(my_string)

my_string = f" the variable is {var*2} and {var2}"
print(my_string)


