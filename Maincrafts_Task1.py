# 1. Sum of Two Numbers - Take input and print their sum

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

c = a + b

print(f"Their sum is {c} ")

# 2. Odd or Even Checker
x = int(input("Enter the number: "))

if x % 2 == 0:
    print("Even")
    else:
    print("Odd")

# 3. Factorial Calculation - Using a loop or recursion
def factorial_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(factorial_loop(7))

# 4. Fibonacci Sequence - Generate first n numbers
n = int(input("How many Fibonacci numbers? "))

a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 5. String Reverse - Reverse user input string
text = input("Enter a string: ")
print("Reversed:", text[::-1])

# 6. Palindrome Check -
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

# 7. Leap Year -
x = int(input("Enter the year: "))

if x % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

# 8. Armstrong Number -
number = int(input("Enter a number: "))

digits = str(number)
power = len(digits)
total = 0

for d in digits:
    total = total + int(d) ** power

if total == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")