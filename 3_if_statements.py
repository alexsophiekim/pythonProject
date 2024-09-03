# If else statements for condition check
# IF - True // Eles - False

age = int(input("Enter your age: "))

if age >= 120:
    print("RIP")
elif age >= 18:
    print("Bottoms up!")
elif age < 0:
    print("You are not a human yet")
else:
    print("Drink milk")

response = input("Would you like food? (Y/N) ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you")


name = input("Enter your name: ")
if name == " ":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

#Bool if-else
for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

online = False

if online:
    print("The user is online")
else:
    print("The user is offline")