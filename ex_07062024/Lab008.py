# Understanding Strings
# This code demonstrates various string operations in Python
# Strings are immutable sequences of characters

# '', "", """
name = "Michael"
print(name)  # Output: Michael

about = """He said - Hello!! """
print(about)  # Output: He said - Hello!!

directory = r'C:\Users\michaelc\Documents'  # Raw string literal
print(directory)  # Output: C:\Users\michaelc\Documents

# Formatting Strings
first_name = "Michael"
last_name = "Jackson"
print(first_name + " " + last_name)
print(first_name, last_name)

# f - used for formatting
print(f"Your full name is{first_name} {last_name}")  # Output: Michael Jackson
print(f'Your full name is {first_name} {last_name}')  # Output: Michael Jackson


num = 98
print(f"Your number is {num}")  # Output: Your number is 98
print(f"Your number is {num *2}")
print(f"Your number is {num *3}")

num = 7
print(f"{num}x1 = {num}")
print(f"{num}x2 = {num*2}")
print(f"{num}x3 = {num*3}")
print(f"{num}x4 = {num*4}")
print(f"{num}x5 = {num*5}")
print(f"{num}x6 = {num*6}")
print(f"{num}x7 = {num*7}")
print(f"{num}x8 = {num*8}")
print(f"{num}x9 = {num*9}")
print(f"{num}x10 = {num*10}")

b = 10
print(f"{b}x5 = {b}")

# to showcase the output using .format
print("2x{}={}".format(b, b*2))

