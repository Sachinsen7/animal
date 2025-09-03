#  Counting positive Numbers 

numbers = [1, -2, 3, 4, -5, 6, -7, 8, -9, 10]
positive_number_count = 0

for num in numbers:
    if(num> 0):
        positive_number_count += 1

print("Final count of positive numbers: ", positive_number_count)



#  sum of even numbers 

num = 10
sum_even = 0

for n in range(1, num + 1):
    if n % 2 == 0:
        sum_even += 1

print(sum_even)


#  multiplication table printer

#  skip fifth iteration 

number = 3

for i in range(1, 11):
    if i == 5:
        continue
    
print(number, 'x', i, "=", number * i)


#  reverse a string 

string = "Python"

reversed_str = ""

for char in string:
    reversed_str = char + reversed_str

print(reversed_str)

#  find the first non repwating character 

input_string = "teeter"

for char in input_string:
    print(char)
    if input_string.count(char) == 1:
        print("Char is: ", char)
        break


#  factorial calculator 

#  using while loop 

number = 5
factorial  = 1

while number > 0: 
    factorial = factorial * number
    number -= 1

print(factorial)


# validate input 

while True:
    nums = input("enter values b/w 1 and 10")
    if 1 <= nums <= 10:
        print("Thanks")
        break
    else: 
        print("Invalid numbers try again")


#  prime numbers

take_input = input("enter a number: ")

is_prime = True

if take_input > 1:
    for i in range(2, number):
        if (take_input % i) == 0:
            is_prime = False
            break

print(is_prime)

# list uniqueness checker

items = ["apple", "banana", "orange", "apple", "mongo"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate")
        break
    unique_item.add(item)
print(unique_item)


#  exponential backoff

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("attempt", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
