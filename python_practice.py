# Python practice

# Create a function called greetings that takes one argument as string and returns the name
def greetings(name):
    return name


print(greetings("bob"))

# Declare a list of numbers from 1 to 9 iterate through the list and print the list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    print(num)

# Write the boolean operators
# if a == b and c == d: print(TRUE)
if "a" == "b" and "c" == "d":
    print(True)

# create a list of five numbers starting from 0
numbers = [0, 1, 2, 3, 4]

# create a tuple with the same information
num_tuple = tuple(numbers)

# change the value to the tuple in the last index

# cannot change a tuple
# because tuples are IMMUTABLE
# unlike lists, that can be changed as they are MUTABLE

# create a dict with two key pairs
# first key is name , and the value of the name is james
# second key is age  value is 18
my_dict = {"name": "James", "age": 18}
# print the value of keys
print(my_dict["name"])
print(my_dict["age"])


# create a class called isobel and initialise that takes two arguments
class Bob:
    def __init__(self, name, date_of_birth):
        self.name = "bob"
        self.date_of_birth = "09/06/2001"


# create an object of that class
person = Bob("bob", "20")
print(person.name)
print(person.date_of_birth)

# write the correct syntax to create a set
set_a = {1, 2, 3, 4}
# difference between sets and all other collections
# Sets are unordered
print(set_a)
set_a.update({5})
print(set_a)


# create a method that takes one argument as a string my name
# if the name == bob return true else false
def is_bob(name):
    if name == "bob":
        return True
    else:
        return False


print(is_bob("bob"))


# create a class called human with one method called breathe that returns breathing
# create another class called student that inherits from human and create object of student class
# and call the function from the parent class
class Human:

    def __init__(self):
        self.alive = True

    def breathe(self):
        return "breathing"


class Student(Human):
    pass


student = Student()
print(student.breathe())


# write the correct syntax to use the keyword super
class Human:

    def __init__(self):
        self.alive = True

    def breathe(self):
        return "breathing"


class Student(Human):
    def __init__(self):
        super().__init__()

# Super refers to the parent class


# Create a variable called user_data and store 0 to 4 in that list
# Create a function that takes an argument as a list
# the function returns True if the datatype is list false otherwise
user_data = [0, 1, 2, 3, 4]


def is_list(a_list):
    if type(a_list) == list:
        return True
    else:
        return False


print(is_list(user_data))


# Create a function called get_percentage, takes two integers as arguments , returns the percentage of two
def get_percentage(num1, num2):
    percent_num1 = (num1/num2) * 100
    return percent_num1


print(get_percentage(10, 90))


# Create a function that takes 2 args as int and divide first value by second value
# returns the outcome
# checks if the numbers given is divisible by 0
# throw an error if cant be divided by 0 else return the value
def division(num1, num2):
    try:
        return int(num1) / int(num2)
    except ZeroDivisionError as error:
        return error


print(division(10, 5))


# Write five odd numbers in a list and then five even numbers in another list
# iterate through these lists to combine and display the numbers in a method
odd_nums = [1, 3, 5, 7, 9]
even_nums = [2, 4, 6, 8, 10]

count = 1
for item in even_nums:
    odd_nums.insert(count, item)
    count += 2
print(odd_nums)

# create a dictionary called shopping list with 3 key value pairs
# milk: £1, yoghurt: £1.15, ice cream: £2.38
# create a function that takes an arg as the dictionary
# iterate through the values of dictionary add the total value and return the total cost
shopping_list = {"milk": 1, "yoghurt": 1.15, "ice cream": 2.38}


def totals(shop):
    sums = 0
    for items in shop.values():
        sums += items
    return sums


print(totals(shopping_list))

# create shopping list and print the cost of yoghurt
shopping_list = {"milk": 1, "yoghurt": 1.15, "ice cream": 2.38}
print(shopping_list["yoghurt"])
