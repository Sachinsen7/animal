#Examples
# I Wake up
# If I'm hungry
# I eat breakfast

# i leave my house
# If it"s cloudy
# I bring an umbrella
# otherwise
#  I bring sunglasses


# I'm at the restaurent
# If i want meat
# i order a steak
# otherwise If i want fastfood
# i order chawmin & pasta
# otherwise
#I order a Salad

is_male = True
if is_male:
    print("You are male")
else:
  print("You are not a male ")


is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")



is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")


is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")




is_male = False
is_tall = True

if is_male and is_tall:
        print("You are a tall male")
elif not(is_male) and is_tall:
    print("Your are not a male but are tall")
else:
    print("you are either not male or not tall or both")










