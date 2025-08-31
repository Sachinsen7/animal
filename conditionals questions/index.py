# Age group categorization

# userscore = input("enter your age")
userage = 25

# age_in_int = int(userscore)


if userage < 13:
    print("Child")
elif userage < 20:
    print("Teen")
elif userage < 60:
    print("Adult")
else:
    print("Senior")


# Movie ticket Pricing 

age = 22 
day = "Wednesday"


price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you$", price)


# Grade Calculator 
score = 85

if score >= 101:
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "D"
elif score >= 60:
    grade = "D"
else:
    grade = "F"


# Fruit Ripeness Checker

fruit = "Banana"
color = "yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")


# Weather Acitivity Suggetion

weather = "sunny"

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "snowy"
elif weather == "snowy":
    activity = "Build a snowman"

print(activity) 



# transportation 

distance = 5

if distance < 3:
    transport = "walk"
elif distance < 10:
    transport = "bicycle"
else:
    transport = "car"

print(transport)


# Coffee customization

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)


#  Password strength checker

password = "Secret123ss@"

if len(password) < 6:
    strength = "Weak"
elif len(password) < 10:
    strength = "Medium"
else:
    strength = "Strong"

print(strength)


#  Leap Year Checker

year = 2025

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year", year)
else:
    print("Not a leap year", year)


#  pet food recommendation

pet_food = "Super"




