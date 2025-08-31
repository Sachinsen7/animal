# 1. Core Number Types
import math

# int

x = 2
y = 3
z = 4

print(x + y)

my_age = 30

temperature = 20

national_dept = 100


print(my_age, temperature, national_dept)


# float


pi_approx = 3.14159


account_balance = -123.45

# Scientific notation 
earth_mass = 5.972e24

print(type(pi_approx))




#  Numeric Operations

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

print(0.1 + 0.2)
# Output: 0.30000000000000004


# complex(Complex Number)
# A complex number with real part 3 and imaginary part 5
z = 3 + 5j

# A purely imaginary number
c = -2j

print(type(z))
# Output: <class 'complex'>

# Accessing parts of the number
print(z.real) # Output: 3.0
print(z.imag) # Output: 5.0 

math.sqrt(2)
math.pow(2, 3)
print(math.pow(2, 3))
print(math.factorial(3))
print(math.gcd(10, 15))
print(math.floor(2.9))
print(math.ceil(2.9))
print(math.e)



# 3. Type Conversions

this_one = 1
that_one = 2.0

print(this_one + that_one)

x = 5          # int
y = 2.8        # float
z = 3 + 2j     # complex

print(float(x))   # 5.0
print(int(y))     # 2
print(complex(x)) # (5+0j)


# 4. Built-in Functions with Numbers

nums = [1, 2, 3, 4, 5]

print(abs(-7))
print(sum(nums))
print(min(nums))
print(max(nums))
print(round(3.4))
print(round(3.6))


# 6. Random Numbers (random module)

import random 

print(random.random())
print(random.randint(1, 10))
print(random.uniform(0, 10))
print(random.choice(nums))


# 7. Decimal and Fractions (for accuracy)

from decimal import Decimal
from fractions import Fraction

x = Decimal("0.1")
y = Decimal("0.2")

print(x + y)


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1 + f2)


int(3, 14)

int(64, 16)

int(3.14)

int(64, 8)


set_one = {1, 2, 3, 4}
set_one & {1, 3}


set_one = {1, 2, 3, 4}
set_one | {1, 3}

type({})

