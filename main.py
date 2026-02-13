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
