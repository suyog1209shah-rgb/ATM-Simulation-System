balance = 10000
pin = "1234"
entered_pin = input("Enter your PIN: ")
if entered_pin == pin:
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            print("Your balance is:", balance)
            elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("Amount deposited successfully.")

