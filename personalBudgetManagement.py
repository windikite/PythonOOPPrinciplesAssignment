from functions import *
from budgetCategory import budgetCategory

def mainLoop():
    categories = {}
    while True:
        user_input = askMenu([
                "Add category to budget", 
                "Add or delete expenses", 
                "View all expenses", 
                "Delete category", 
                "Quit"], 
                "Please choose an operation: ")
        try:
            user_input = int(user_input)
            if user_input == 0:
                category_name = str(input("Please enter a category name: "))
                if category_name not in categories:
                    category_budget = float(input(f"Please input a budget for {category_name}: "))
                    new_category = budgetCategory(category_name, category_budget)
                    categories.update({category_name: new_category})
                else:
                    print(f'Category "{category_name}"already exists!')
            elif user_input == 1:
                category_names = [category[0] for category in list(categories.items())]
                index_to_edit = int(askMenu(category_names, "Please choose a category to edit: "))
                name_to_edit = list(category_names)[index_to_edit]
                mode = int(askMenu(["Add expense", "Delete expense"], "Please choose an operation: "))
                if mode == 0:
                    expense_name = str(input("Please enter the name of the expense: "))
                    expense = float(input(f"Please input the cost of {expense_name}: "))
                    categories.get(name_to_edit).addExpense(expense_name, expense)
                elif mode == 1:
                    expenses = categories.get(name_to_edit).getExpenses()
                    expense_names = [expense[0] for expense in list(expenses.items())]
                    index_to_delete = int(askMenu(expense_names, "Please choose an expense to delete: "))
                    expense_to_delete = list(expense_names)[index_to_delete]
                    categories.get(name_to_edit).removeExpense(expense_to_delete)
            elif user_input == 2:
                if len(categories.items()) > 0:
                    for category in categories.items():
                        category[1].getInfo()
                else:
                    print("Please create a category first.")
            elif user_input == 3:
                category_names = [category[0] for category in list(categories.items())]
                index_to_edit = int(askMenu(category_names, "Please choose a category to delete: "))
                name_to_delete = list(category_names)[index_to_edit]
                categories.pop(name_to_delete)
            elif user_input == 4:
                break
        except Exception as e:
            printCritical(e)
        else:
            printSuccess("Done!")


mainLoop()