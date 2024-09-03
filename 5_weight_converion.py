#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("KGs or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"

else:
    print(f"Error - {unit} is not valid")

print(f"Your weight is {round(weight,2)} {unit}")