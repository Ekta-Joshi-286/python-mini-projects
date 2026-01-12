# Expense Tracker

# Step 1: Create an empty list to store expenses
expenses = []

# Step 2: Function to add a new expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    expenses.append({"date": date, "category": category, "amount": amount})
    print("✅ Expense added successfully!")

# Step 3: Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n------ ALL EXPENSES ------")
    for e in expenses:
        print(f"Date: {e['date']} | Category: {e['category']} | Amount: ₹{e['amount']}")

# Step 4: Function to show total per category
def total_per_category():
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]

    print("\n------ TOTAL PER CATEGORY ------")
    for cat, total in totals.items():
        print(f"{cat}: ₹{total}")

# Step 5: Function to show monthly summary
def monthly_summary():
    totals = {}
    for e in expenses:
        month = e["date"][3:5]  # Extract month from DD-MM-YYYY
        totals[month] = totals.get(month, 0) + e["amount"]

    print("\n------ MONTHLY SUMMARY ------")
    for month, total in totals.items():
        print(f"Month {month}: ₹{total}")

# Step 6: Main program loop
while True:
    print("\n------ EXPENSE TRACKER MENU ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total per Category")
    print("4. Monthly Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_per_category()
    elif choice == "4":
        monthly_summary()
    elif choice == "5":
        print("👋 Exiting Expense Tracker. Stay within your budget!")
        break
    else:
        print("Invalid choice. Please try again.")
