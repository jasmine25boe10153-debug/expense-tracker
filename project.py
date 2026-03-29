import json

FILE_NAME = "expenses.txt"

# Load existing data
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save data
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)

expenses = load_expenses()

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food/travel/etc): ")
    
    expenses.append({"amount": amount, "category": category})
    save_expenses(expenses)
    
    print("Expense added & saved!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} - ₹{exp['amount']}")
    print()

def total_spending():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending: ₹{total}\n")

def highest_expense():
    if not expenses:
        print("No expenses yet.\n")
        return
    highest = max(expenses, key=lambda x: x["amount"])
    print(f"Highest expense: {highest['category']} - ₹{highest['amount']}\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Highest Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        highest_expense()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")