# Personal Mini-Toolkit
# A menu-driven program with a calculator, a to-do list, and a guessing game.

def calculator():
    """Ask for two numbers and calculate a result."""
    print("\n--- Simple Calculator ---")
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ").strip()

        if operation == "+":
            answer = first + second
        elif operation == "-":
            answer = first - second
        elif operation == "*":
            answer = first * second
        elif operation == "/":
            if second == 0:
                print("Sorry, you cannot divide by zero.")
                return
            answer = first / second
        else:
            print("That operation is not available. Please choose +, -, *, or /.")
            return

        print(f"Your answer is: {answer:g}")
    except ValueError:
        print("Please enter valid numbers and try again.")


def todo_list(tasks):
    """Allow the user to add, view, and remove tasks from a changing list."""
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Return to main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("Here are your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "2":
            task = input("Enter the task to add: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("The task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                try:
                    number = int(input("Enter the task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("That task number is not on the list.")
                except ValueError:
                    print("Please enter a whole number.")
        elif choice == "4":
            return
        else:
            print("Please choose 1, 2, 3, or 4.")


def guessing_game():
    """Keep asking for a guess until the user finds the secret number."""
    secret_number = 7
    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number from 1 to 10.")

    while True:
        try:
            guess = int(input("Your guess (1-10): "))
            if guess < 1 or guess > 10:
                print("Please choose a number from 1 to 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! The secret number was {secret_number}. Well done!")
                break
        except ValueError:
            print("Please enter a whole number.")


def main():
    """Keep showing the menu until the user chooses to quit."""
    tasks = []

    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\n========================================")
        print("Choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list(tasks)
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"'{choice}' is not a menu option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
