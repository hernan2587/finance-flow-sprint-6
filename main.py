"""

Name: Hernan Ramoz

Course: ADD-100

Project: Finance Flow

Description:

This program helps users understand their monthly finances.

It asks for income, expenses, and debt payments.

Then it creates a FinanceAccount object and displays the balance.

"""

from finance_account import FinanceAccount

# Global Constants

WELCOME_MESSAGE = "Welcome to Finance Flow"

PROGRAM_MESSAGE = "This program helps you understand your monthly finances.\n"

ERROR_MESSAGE = "Invalid input. Please enter numbers only."

def show_welcome():

    print(WELCOME_MESSAGE)

    print(PROGRAM_MESSAGE)

def read_menu():

    income_label = "monthly income"

    expense_label = "monthly expenses"

    debt_label = "monthly debt payments"

    try:

        file = open("finance_menu.txt", "r")

        for line in file:

            line = line.strip()

            parts = line.split(":")

            if parts[0] == "INCOME_LABEL":

                income_label = parts[1].strip()

            elif parts[0] == "EXPENSE_LABEL":

                expense_label = parts[1].strip()

            elif parts[0] == "DEBT_LABEL":

                debt_label = parts[1].strip()

        file.close()

    except FileNotFoundError:

        print("Error: file not found")

    return income_label, expense_label, debt_label

def get_number(prompt):

    while True:

        try:

            number = float(input(prompt))

            return number

        except ValueError:

            print(ERROR_MESSAGE)

def get_income(label):

    return get_number("Enter your " + label + ": ")

def get_expenses(label):

    return get_number("Enter your " + label + ": ")

def get_debt(label):

    return get_number("Enter your " + label + ": ")

def save_to_file(balance):

    with open("finance_log.txt", "a") as file:

        file.write("Balance: " + str(balance) + "\n")

def save_report(balance):

    with open("finance_report.txt", "w") as file:

        file.write("Financial Report\n")

        file.write("--------------------\n")

        file.write("Balance: " + str(balance) + "\n")

        if balance < 0:

            file.write("Warning: You are spending more than you earn.\n")

        elif balance == 0:

            file.write("You have no money left this month.\n")

        else:

            file.write("Good job! You still have money left.\n")

def main():

    show_welcome()

    income_label, expense_label, debt_label = read_menu()

    income = get_income(income_label)

    expenses = get_expenses(expense_label)

    debt = get_debt(debt_label)

    account = FinanceAccount(income, expenses, debt)

    account.display_summary()

    balance = account.calculate_balance()

    save_to_file(balance)

    save_report(balance)

main()