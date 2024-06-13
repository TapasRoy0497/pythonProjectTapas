# Develop a Python script that calculates the square and cube of a given number.
# num = 2 sq - 4, c = 8
num = int(input("Enter a number: "))
square = num ** 2   # Will calculate the square
cube = num ** 3     # Will calculate the cube
print(f"The square of {num} is {square}")
print(f"The cube of {num} is {cube}")

# Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")