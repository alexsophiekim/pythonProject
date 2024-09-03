# This is my first Python learning
from operator import itemgetter

print("Hello World!")
print("It's rainy day.")

#Variables (str,int,float,bool)

#String
first_name = "Sophie"
food = "Sushi"
email = "sophie@fake.com"
print(type(first_name))
print(first_name)
#f-string f: format
print(f"Hello {first_name}")

#Integers
age = 30
quantity = 3
num_of_students = 25

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float - still number but decimal
price= 10.99
gpa = 3.2
distance = 5.5

print(f"This item price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

#Bool
is_student = False
for_sale = True
print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")


if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT available")

#Typecasting = the process of converting a variable from one data type to another str(),int(),float(),bool()

name = "Sophie"
age = 30
gpa = 3.2
is_student = True

print(type(age))
gpa = int(gpa) #convert decimal to int
print(gpa)

age = str(age)
print(age)
print(type(age))  #output class 'str'


#input() = A function that prompts the user to enter data Returns the entered data as a string
name = input("What is your name?: ")
print(f"Hello {name}!")

#Exercise 1 Rectangle area calc
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is: {area}㎠")

#Exercise 2 Shopping Cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total amount is ${total}")

#Madlibs game
#word game where you create a story
#by filling in blanks with random words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with -ing: ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
#
