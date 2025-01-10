from services import add_expense, get_expenses
from initialize_db import initialize_db
from notifications import send_sms
import warnings 
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

def main():
    initialize_db()

    # Testing
    expense = add_expense("Food", 20.5, "Lunch at a resturaunt")

    if expense:
        send_sms = ("+12105521482", f"New expense added: {expense.category}, ${expense.amount} - {expense.description}")

    for expense in get_expenses():
        print(expense)

if __name__ == "__main__":
    main()