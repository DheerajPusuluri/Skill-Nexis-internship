balance = 5000
correct_pin = "1234"
def check_balance():
    print("Your current balance is: ₹", balance)
def deposit():
    global balance
    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
        print("New balance: ₹", balance)
    else:
        print("Invalid amount.")
def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance: ₹", balance)
pin = input("Enter your PIN: ")
if pin == correct_pin:
    print("\nLogin successful!")
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Access denied.")