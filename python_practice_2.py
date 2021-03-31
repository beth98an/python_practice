# Create a function called greetings that takes one argument as string and returns the name
def greeting(name):
    return name


# Declare a list of numbers from 1 to 9 iterate through the list and print the list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num:
    print(i)

# Write the boolean operators
# if a == b and c == d: print(TRUE)
if "a" == "b" and "c" == "d":
    print(True)

# Create a list of five numbers starting from 0
# Create a tuple with the same information
# Change the value to the tuple in the last index

numbers = [0, 1, 2, 3, 4]
tuple_numbers = tuple(numbers)
# IMMUTABLE cannot change last number

# Create a dict with two key pairs
# First key is name , and the value of the name is james
# Second key is age value is 18
# Print the value of keys
person = {"name": "James", "age": 18}
print(person.values())


# Create a class called bob and initialise so that it takes two arguments
# Create an object of that class
class Bob:
    def __init__(self, name, age):
        self.name = name
        self.age = age


guy = Bob("bobby", 27)
print(guy.name)

# Write the correct syntax to create a set
# Difference between sets and all other collections
a_set = {1, 3, 34, "a string"}
# Sets are unordered


# Create a method that takes one argument as a string my name
# If the name == bob return true else false
def funky(name):
    if name == "bob":
        return True
    else:
        return False


print(funky("not bob"))


# Create a class called human with one method called breathe that returns breathing
# Create another class called student that inherits from human
# and create an object of student class and call the function from the parent class
# write the correct syntax to use the keyword super

class Human:
    def __init__(self):
        self.alive = True

    def breathe(self):
        return "breathing"


class Student(Human):
    def __init__(self):
        super().__init__()


student = Student()
print(student.breathe())

# Create a variable called user_data and store 0 to 4 in that list
# Create a function that takes an argument as a list the function returns True if the datatype is list false otherwise
user_data = [0, 1, 2, 3, 4]


def is_a_list(a_list):
    if type(a_list) == list:
        return True
    else:
        return False


print(is_a_list(user_data))


# Create a function called get_percentage, takes two integers as arguments , returns the percentage of two
def get_percentage(num1, num2):
    return (num1 / num2) * 100


print(get_percentage(70, 95))


# Create a function that takes 2 args as int and divide first value by second value
# returns the outcome
# checks if the numbers given is divisible by 0 throws an error if can't be divided by 0 else return the value
def divide(arg1, arg2):
    try:
        return int(arg1) / int(arg2)
    except ZeroDivisionError as error:
        return error


print(divide(2, 7))

# Write five odd numbers in a list and then five even numbers in another list iterate through these lists to combine and display the numbers in a method
odd_nums = [1, 3, 5, 7, 9]
even_nums = [2, 4, 6, 8, 10]
i = 1
for item in even_nums:
    odd_nums.insert(i, item)
    i += 2

# Create a dictionary called shopping list with 3 key value pairs milk: £1, yoghurt: £1.15, ice cream: £2.38
# create a function that takes an arg as the dictionary
# iterate through the values of dictionary add the total value and return the total cost
# Create shopping list and print the cost of yoghurt

shopping_list = {"milk": 1, "yoghurt": 1.15, "ice cream": 2.38}
print(shopping_list["yoghurt"])


def total_cost(shop):
    total = 0
    for value in shop.values():
        total += value
    return total


print(total_cost(shopping_list))

