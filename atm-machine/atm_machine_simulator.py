# Step 1: Store user details in a dictionary
users = {
    'user1': {'pin': 1234, 'balance': 10000},
    'user2': {'pin': 5678, 'balance': 5000}
}
# Step 2: Define functions for ATM operations
def check_balance(user):
    print(f"Your current balance is: ₹{users[user]['balance']}")

def deposit_cash(user):
    amount = int(input("Enter amount to deposit: ₹"))
    if amount > 0:
        users[user]['balance'] += amount
        print(f"₹{amount} deposited successfully.")
        check_balance(user)
    else:
        print("Invalid amount.")

def withdraw_cash(user):
    amount = int(input("Enter amount to withdraw: ₹"))
    if 0 < amount <= users[user]['balance']:
        users[user]['balance'] -= amount
        print(f"₹{amount} withdrawn successfully.")
        check_balance(user)
    else:
        print("Insufficient balance or invalid amount.")

def atm_menu(user):
    while True:
        print("\n------ ATM MENU ------")
        print("1. Balance Inquiry")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_balance(user)
        elif choice == '2':
            deposit_cash(user)
        elif choice == '3':
            withdraw_cash(user)
        elif choice == '4':
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
# Step 3: Main Program Loop
print("---------- Welcome to Python Bank ATM ----------")

while True:
    user_id = input("\nEnter your user ID (or 'exit' to quit): ")
    if user_id.lower() == 'exit':
        print("Goodbye!")
        break

    if user_id in users:
        pin = int(input("Enter your PIN: "))
        if pin == users[user_id]['pin']:
            print("Login successful!")
            atm_menu(user_id)
        else:
            print("Incorrect PIN. Try again.")
    else:
        print("User not found. Try again.")

