# 1. Leap Year Checker:
#    Create a program that determines whether a given year is a leap year.
#    A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#    Use an if-else statement to make this determination.
#    Input = 2024
#    Output = Leap year

year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# 2. Triangle Classifier:
#   Write a program that classifies a triangle based on its side lengths.
#   Given three input values representing the lengths of the sides,
#   determine if the triangle is equilateral (all sides are equal),
#   isosceles (exactly two sides are equal), or scalene (no sides are equal).
#   Use an if-else statement to classify the triangle.
#   3 Inputs
#   side 1, side 2 and side 3
#   output - Equilateral, Isosceles, Scalene -
#   Equilateral. = side 1 == side 2 = side 3
#   Isosceles = side 1 == side 2 or side 2 == side 3 or side 1 == side 3
#   Scalene = no sides are equal

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# 3. Factorial: find the factorial of a given number.
#   n = 5
#   5! -->5*4*3*2*1 -> 120
#   3! -> 3*2*1 -> 6
n = int(input("Enter a number to find its factorial: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n} is {fact}")

# 4. Fibonacci series
#   0,0+1, 0+1+1,
#   n = 7
#   0, 1, 2, 3, 5, 8, 13

FiboRange = int(input("Enter the number of terms of Fibonacci series to be printed: "))
first = 0
second = 1
if FiboRange <= 0:
    print("Please enter a positive number")
else:
    print(f"Fibonacci series up to {FiboRange} terms is:")
    print(first, end=" ")
    for x in range(1, FiboRange):
        print(second, end=" ")
        next = first + second
        first = second
        second = next
