import csv


expenses = []


def add_expense():

    item = input("Enter expense name: ")

    amount = float(input("Enter amount: "))

    expense = {
        "item": item,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added")


def view_expenses():

    print("\n--- EXPENSES ---")

    for expense in expenses:

        print(
            expense["item"],
            "-",
            expense["amount"]
        )


def total_expense():

    total = 0

    for expense in expenses:

        total += expense["amount"]

    print("Total Expense:", total)


def save_expenses():

    with open(
        "expenses.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(["Item", "Amount"])

        for expense in expenses:

            writer.writerow([
                expense["item"],
                expense["amount"]
            ])

    print("Expenses saved")


while True:

    print("\n--- EXPENSE TRACKER ---")

    print("1. Add Expense")

    print("2. View Expenses")

    print("3. Total Expense")

    print("4. Save Expenses")

    print("5. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        add_expense()


    elif choice == "2":

        view_expenses()


    elif choice == "3":

        total_expense()


    elif choice == "4":

        save_expenses()


    elif choice == "5":

        print("Program closed")

        break


    else:

        print("Invalid choice")