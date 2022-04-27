import random


def title():
    print("Math Quiz in Python")


def options():
    options_list = ["1. Multiplication", "2. Addition", "3. Division", "4. Subtraction", "5. Quit game"]
    print(options_list[0])
    print(options_list[1])
    print(options_list[2])
    print(options_list[3])
    print(options_list[4])


def option_input():
    choice = int(input("Please select an option: "))
    while choice > 5 or choice <= 0:
        print("Option selected not available.")
        choice = int(input("Please select an option between 1 - 5: "))
    else:
        return choice


def get_answer(question):
    print("What is your answer?")
    print(question, end="")
    solution = float(input(" = "))
    return solution


def verify_answer(answer, result, x):
    if answer == result:
        x = x + 1
        print("Answer is correct! Great work")
        return x
    else:
        print("Wrong answer provided")
        return x


def options_items(choice, x):
    first_number = random.randrange(1, 21)
    second_number = random.randrange(1, 21)
    if choice == 1:
        question = str(first_number) + " * " + str(second_number)
        result = first_number * second_number
        answer = get_answer(question)
        x = verify_answer(answer, result, x)
        return x
    elif choice == 2:
        question = str(first_number) + " + " + str(second_number)
        result = first_number + second_number
        answer = get_answer(question)
        x = verify_answer(answer, result, x)
        return x
    elif choice == 3:
        question = str(first_number) + " / " + str(second_number)
        result = first_number / second_number
        answer = get_answer(question)
        x = verify_answer(answer, result, x)
        return x
    else:
        question = str(first_number) + " - " + str(second_number)
        result = first_number - second_number
        answer = get_answer(question)
        x = verify_answer(answer, result, x)
        return x


def show_score(sum, valid):
    if sum > 0:
        score = valid / sum
        percentage = round((score * 100), 2)
    if sum == 0:
        percentage = 0
    print(sum, "questions were answered", ",", valid, "were correct.")
    print("Your total score is ", percentage, "%. Thank you for playing this game.", sep = "")


def main():
    title()
    options()

    option = option_input()
    sum = 0
    valid = 0
    while option != 5:
        sum = sum + 1
        valid = options_items(option, valid)
        option = option_input()

    print("Quit game.")
    # display_separator()
    show_score(sum, valid)


main()
