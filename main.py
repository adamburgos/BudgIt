from services import add_expense, get_expenses

def main():
    add_expense("Food", 20.5, "Lunch at a resturaunt")
    add_expense("Transport", 15.6, "Uber ride")

    for expense in get_expenses():
        print(expense)

if __name__ == "__main__":
    main()