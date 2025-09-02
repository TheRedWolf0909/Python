# Task 1: Perform Basic Mathematical Operations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("\n")

# Addition

sum_result = num1 + num2
print("Addition:", sum_result, "\n")

# Subtraction

sub_result = num1 - num2
print("Subtraction:", sub_result, "\n")

# Multiplication

mult_result = num1 * num2
print("Multiplication:", mult_result, "\n")

# Division

if num2 != 0:
    div_result = num1 / num2
    print("Division:", div_result, "\n")


# Task 2: Create a Personalized Greeting

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("\n")

full_name = first_name + " " + last_name

print("Hello, " + full_name + "! Welcome to the Python programming world.")