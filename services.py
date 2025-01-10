import sqlite3
from models import Expense 

expenses = []

def add_expense(category, amount, description):
    new_expense = Expense(category, amount, description)

    conn = sqlite3.connect("budgit.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM expenses WHERE id = ?", (new_expense.id,))
    if cursor.fetchone():
        print(f"Expense with ID {new_expense.id} already exists. Skipping insertion.")
        conn.close()
        return new_expense

    cursor.execute(""" INSERT INTO expenses 
    (id, category, amount, date, description) 
    VALUES (?, ?, ?, ?, ?) """, 
    (new_expense.id, new_expense.category, new_expense.amount, new_expense.date.isoformat(), new_expense.description))

    conn.commit()
    conn.close()

    print(f"Expense added: {new_expense}")
    return new_expense

def get_expenses():
    conn = sqlite3.connect("budgit.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    expenses = []
    for row in rows:
        expense = Expense(
            id=row[0],
            category=row[1], 
            amount=row[2], 
            date=row[3],
            description=row[4]
            )
        expenses.append(expense)

    conn.close()
    return expenses