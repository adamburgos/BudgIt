from models import Expense 

expenses = []

def add_expense(category, amount, description):
    new_expense = Expense(category, amount, description)
    expenses.append(new_expense)
    return new_expense

def get_expenses():
    return expenses