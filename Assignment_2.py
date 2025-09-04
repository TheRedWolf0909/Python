# Task 1: Check if a Number is Even or Odd

a = int(input("Enter a number: "))

if a % 2 == 0:
    print(a, "is an even number.")
else:
    print(a, "is an odd number.")


# Task 2: Sum of Integers from x to y Using a Loop

x = int(input("Enter the starting integer (x): "))
y = int(input("Enter the ending integer (y): "))

sum = 0

for i in range(x, y + 1):
    sum += i
print("The sum of numbers from", x, "to", y, "is: ", sum)
