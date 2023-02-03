class Account:
    def __init__(self, account_number, balance=100):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount >= 100:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount

accounts = {}

while True:
    print("1. Create a new account")
    print("2. Deposit to an account")
    print("3. Withdraw from an account")
    print("4. Display the account with the highest balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_number = int(input("Enter the account number: "))
        balance = int(input("Enter the initial balance (default 100): "))
        accounts[account_number] = Account(account_number, balance)
    elif choice == 2:
        account_number = int(input("Enter the account number: "))
        if account_number not in accounts:
            print("Error: Account not found")
        else:
            amount = int(input("Enter the amount to deposit: "))
            accounts[account_number].deposit(amount)
    elif choice == 3:
        account_number = int(input("Enter the account number: "))
        if account_number not in accounts:
            print("Error: Account not found")
        else:
            amount = int(input("Enter the amount to withdraw: "))
            success = accounts[account_number].withdraw(amount)
            if not success:
                print("Error: Not enough balance")
    elif choice == 4:
        max_balance = 0
        max_account = None
        for account in accounts.values():
            if account.balance > max_balance:
                max_balance = account.balance
                max_account = account
        if max_account:
            print("Account with the highest balance:")
            print("Account number:", max_account.account_number)
            print("Balance:", max_account.balance)
        else:
            print("Error: No accounts found")
    elif choice == 5:
        break
    else:
        print("Error: Invalid choice")
