unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = input("Enter the temperature: ")

if unit == "C":
    temp = round((9 * float(temp)) / 5 + 32, 1)
    unit = "Fahrenheit"
    print(f"The temperature in {unit} is: {temp}°F")
elif unit == "F":
    temp = round((float(temp)-32)* 5/9,1)
    unit = "Celsius"
    print(f"The temperature in {unit} is: {temp}°C")
else:
    print(f"Error - {unit} is not valid")