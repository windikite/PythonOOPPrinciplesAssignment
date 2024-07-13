from functions import *

# This class accepts a name and budget variable, and from there allows for the following functionality:
# The getting and setting of those variables
# The addition of individual expenses using addExpense()
# The retrieval of the category's info using getInfo()
# The retrieval of a dictionary of expenses as well as remaining funds
# All variables are privately encapsulated and secure against direct editing


class budgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__expenses = {}

    def getName(self):
        return self.__name
    
    def setName(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("New name is not a string.")

    def getBudget(self):
        return self.__budget
    
    def setBudget(self, new_budget):
        if (isinstance(new_budget, float) or isinstance(new_budget, int) and new_budget >= 0):
            self.__budget = new_budget
        else:
            print("New budget is not a positive decimal or non-decimal number.")

    def getInfo(self):
        remaining_funds = self.getRemainingFunds()
        print(f"{capitalizeFirstLetter(self.__name)}:")
        print(f"{self.__budget} is budgeted for {self.__name}. There are {len(self.__expenses.items())} expenses with {remaining_funds} leftover.")
        expense_strings = [f" - {expense[0]} - {expense[1]}" for expense in self.__expenses.items()]
        print("\n".join(expense_strings))

    def addExpense(self, expense_name, expense_cost):
        if isinstance(expense_name, str):
            if (isinstance(expense_cost, float) or isinstance(expense_cost, int) and expense_cost >= 0):
                if self.getRemainingFunds() >= expense_cost:
                    if expense_name not in self.__expenses:
                        self.__expenses.update({expense_name: expense_cost})
                    else:
                        print("Expense already exists!")
                else:
                    print(f"There aren't enough funds left for {expense_name}.")
            else:
                print("New expense cost is not a positive decimal or non-decimal number.")
        else:
            print("New expense name is not a string.")
    
    def removeExpense(self, expense_name):
        if isinstance(expense_name, str):
            if expense_name in self.__expenses:
                self.__expenses.pop(expense_name)
            else:
                print("Expense does not exist.")
        else:
            print("Expense name is not a string.")
    
    def getExpenses(self):
        return self.__expenses
    
    def getRemainingFunds(self):
        expended_money = 0
        for expense in self.__expenses.items():
            expended_money += expense[1]
        return self.__budget - expended_money
        


# new_budget_category = budgetCategory("Electronics", 1000)
# print("Budget name", new_budget_category.getName())
# print("Budget", new_budget_category.getBudget())
# new_budget_category.getInfo()
# new_budget_category.setBudget(-200)
# print("Budget", new_budget_category.getBudget())
# new_budget_category.setBudget(500)
# print("Budget", new_budget_category.getBudget())
# new_budget_category.setName(1)
# print("Budget name", new_budget_category.getName())
# new_budget_category.setName("Cool electronics")
# print("Budget name", new_budget_category.getName())
# print("---------------")
# new_budget_category.addExpense("Internet", 300)
# new_budget_category.addExpense("Games", 50)
# print("Budget", new_budget_category.getBudget())
# print("Expenses", new_budget_category.getExpenses())
# new_budget_category.getInfo()
# print("---------------")
# new_budget_category.addExpense("PS5", 500)
# new_budget_category.addExpense("Controller", 50)
# new_budget_category.getInfo()