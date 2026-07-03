# task1.py
# All 8 challenges in a single Python file

# 1. Sum of Two Numbers
def sum_two_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)


# 2. Odd or Even Checker
def odd_even_checker():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# 3. Factorial Calculation
def factorial_calculation():
    n = int(input("Enter a number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)


# 4. Fibonacci Sequence
def fibonacci_sequence():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# 5. String Reverse
def string_reverse():
    text = input("Enter a string: ")
    print("Reversed String:", text[::-1])


# 6. Palindrome Check
def palindrome_check():
    word = input("Enter a word: ")
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")


# 7. Leap Year Check
def leap_year_check():
    year = int(input("Enter a year: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")


# 8. Armstrong Number Check
def armstrong_number():
    num = int(input("Enter a number: "))
    digits = str(num)
    power = len(digits)

    total = 0
    for digit in digits:
        total += int(digit) ** power

    if total == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


# Menu Driven Program
while True:
    print("\n===== TASK 1 MENU =====")
    print("1. Sum of Two Numbers")
    print("2. Odd or Even Checker")
    print("3. Factorial Calculation")
    print("4. Fibonacci Sequence")
    print("5. String Reverse")
    print("6. Palindrome Check")
    print("7. Leap Year Check")
    print("8. Armstrong Number")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        sum_two_numbers()
    elif choice == '2':
        odd_even_checker()
    elif choice == '3':
        factorial_calculation()
    elif choice == '4':
        fibonacci_sequence()
    elif choice == '5':
        string_reverse()
    elif choice == '6':
        palindrome_check()
    elif choice == '7':
        leap_year_check()
    elif choice == '8':
        armstrong_number()
    elif choice == '9':
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try Again.")
