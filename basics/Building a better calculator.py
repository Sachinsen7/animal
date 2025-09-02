num1 = float(input("Enter a first number:"))
op = input("enter operator:")
num2 = float(input("Enter a second number:"))

if op == "+":
   print(num1 + num2)
elif op == "-":
   print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")