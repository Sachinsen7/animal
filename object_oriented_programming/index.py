# basic class and object 

class Car:

    total_car = 0

    def __init__(self, brand, model): # this is a constructor function
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    # Encapsulation
    def get_brand(self):
        return self.__brand + " !"

    # class method and selfs
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    # Polymorphism
    
    def fuel_type(self):
        return "Petrol"
    

my_car = Car("toyota", "corolla")
# print(my_car.__brand) # private variable
print(my_car.model)
print(my_car.full_name())


# you cannot access private variable outside the class

my_new_car = Car("Honda", "Civic")
# print(my_new_car.brand)
print(my_new_car.model)


# Inheritance


class ELectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # super keyword
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric"

my_tesla = ELectricCar("Tesla", "Model 3", 100)
print(my_tesla.full_name())
print(my_tesla.battery_size)
print(my_tesla.fuel_type())

safari = Car("Safari", "Safari")
safari2 = Car("Tata", "Nexon")
print(safari.fuel_type())
test = Car("test", "test")
print(test.total_car)



print(Car.total_car)


# static method

class Math:
    @staticmethod  # static method => decorators
    def add(a, b):
        return a + b

print(Math.add(1, 2)) # only accessible by class



#  property decorator

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
Person = Person("John", "Doe")
print(Person.full_name)

# isinstance 

print(isinstance(Person, Person))


# multiple inheritance


class Battery:
    def batter_info(self):
        return "Battery info"


class Engine:
    def engine_info(self):
        return "Engine info"


class ElectricCarTwo(Battery, Engine):
    pass

my_new_car = ElectricCarTwo()
print(my_new_car.batter_info())
print(my_new_car.engine_info())