import os
import re
import sys

def main():
    print_menu()
    manage_user_input()
  
def print_menu():
    os.system("cls" if os.name == "nt" else "clear")

    print("Welcome to Workout Tracker!")
    print("---------------------------")
    print("1. Display workout history")
    print("2. Add workout")
    print("3. Delete workout")
    print("4. Display progress")
    print("5. Display goals")
    print("6. Add goal")
    print("7. Delete goal")
    print("8. Quit\n")


def manage_user_input():
    
    while True:
        text = input("> ")

        if input := re.search(r"^([1-8]\.?)$", text):
            action_number = input.group(0)
            break

    match action_number.replace(".", ""):
        case "1":
            #display_workout_history()
            ...
        case "2":
            add_workout()
            ...
        case "3":
            delete_workout()
            ...
        case "4":
            #display_progress()
            ...
        case "5":
            #display_goals()
            ...
        case "6":
            #add_goal()
            ...
        case "7":
            #delete_goal()
            ...
        case "8":
            sys.exit()


def add_workout():
    ...


def delete_workout():
    ...


if __name__ == "__main__":
    main()

