checking_total = 0
savings_total = 0
emergency_fund_total = 0
print("Enter the names and balances of bank accounts (type: quit when done)")
while True:
    account = input("What is the name of this account? ")
    if account == "checking":
        checking_balance = float(input("What is the balance of the account? "))
        checking_total += checking_balance
    elif account == "savings":
        savings_balance = float(input("What is the balance of the account? "))
        checking_total += savings_balance
    elif account == "emergency fund":
        emergency_fund_balance = float(input("What is the balance of the account? "))
        emergency_fund_total += emergency_fund_balance
    elif account == "quit":
        total  = checking_total+savings_total+emergency_fund_total
        print()
        print("Account Information:")
        print(f"checking - {checking_total}")
        print(f"savings - {savings_total}")
        print(f"emergency fund - {emergency_fund_total}")
        print()
        print(f"Total: ${total}")
        print(f"Average: ${total/3:.2f}")
        exit()
    else:
        print("Invalid account")