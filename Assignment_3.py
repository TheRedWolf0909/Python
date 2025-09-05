# Task 1: Calculate Factorial Using a Function

def fectorial(n):

    if(n == 0 or n == 1):
        return 1
    else:
        return n * fectorial(n - 1)

n = int(input("Enter a number: "))

ans = fectorial(n)
print("Factorial of", n, "is:", ans)


# Task 2: Using the Math Module for Calculations

n = int(input("Enter a number: "))

import math

square_root = math.sqrt(n)
print("Square root: ", square_root)

logarithm = math.log(n)
print("Logarithm:", logarithm)

sine = math.sin(n)
print("Sine:", sine)