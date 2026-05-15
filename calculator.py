def add(a, b):

    return a + b


def sub(a, b):

    return a - b


def mul(a, b):

    return a * b


def div(a, b):

    return a / b


while True:

    print("\n--- SMART CALCULATOR ---")

    print("1. Add")

    print("2. Subtract")

    print("3. Multiply")

    print("4. Divide")

    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":

        print("Calculator closed")

        break

    try:

        a = int(input("Enter first number: "))

        b = int(input("Enter second number: "))

        if choice == "1":

            print("Result:", add(a, b))

        elif choice == "2":

            print("Result:", sub(a, b))

        elif choice == "3":

            print("Result:", mul(a, b))

        elif choice == "4":

            print("Result:", div(a, b))

        else:

            print("Invalid choice")

    except:

        print("Invalid input")