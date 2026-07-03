import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    desc = input("Enter expense description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    print("\n--- Expenses ---")
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"Item: {row[0]}, Amount: ₹{row[1]}")

def total_spent():
    total = 0

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            total += float(row[1])

    print(f"Total Spent: ₹{total}")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
