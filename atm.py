user_account = {
  "Balance" : 1000,
  "Pin" : 1234
}

def display_menu():
    #Display the ATM menu options.
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

def check_balance():
   # Display the current balance.
    print(f"Your current balance is: ${user_account['Balance']}")

def deposit_money():
    #Allow the user to deposit money into their account.
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            user_account["Balance"] += amount
            print(f"${amount} deposited successfully. New balance: ${user_account['Balance']}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def withdraw_money():
   # Allow the user to withdraw money from their account.
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > user_account["Balance"]:
            print("Insufficient funds.")
        else:
            user_account["Balance"] -= amount
            print(f"${amount} withdrawn successfully. New balance: ${user_account['Balance']}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def change_pin():
    #Allow the user to change their PIN.
    try:
        new_pin = int(input("Enter your new PIN (4 digits): "))
        if 1000 <= new_pin <= 9999:
            user_account["pin"] = new_pin
            print("PIN changed successfully.")
        else:
            print("PIN must be a 4-digit number.")
    except ValueError:
        print("Invalid input! Please enter a 4-digit number.")

def authenticate_user():
   # Authenticate the user by verifying the PIN.
    for _ in range(3):  # Allow 3 attempts
        try:
            entered_pin = int(input("Enter your PIN: "))
            if entered_pin == user_account["Pin"]:
                return True
            else:
                print("Incorrect PIN. Try again.")
        except ValueError:
            print("Invalid input! Please enter a numeric PIN.")
    print("Too many incorrect attempts. Exiting...")
    return False

def atm_simulation():
    #Main function to run the ATM simulation.
    print("Welcome to the ATM!")
    if not authenticate_user():
        return

    while True:
        display_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit_money()
            elif choice == 3:
                withdraw_money()
            elif choice == 4:
                change_pin()
            elif choice == 5:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
atm_simulation()
