lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Kevin"))

friends = ["Kevin",  "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends)
