
#create bank account
#amount depositing
#amount witdrawing
#account holdername

class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_number, name, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = {'name': name, 'balance': initial_balance}
            print("Account created successfully.")
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print("Deposit successful.")
        else:
            print("Account not found.")
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")
    def account_details(self, account_number):
        if account_number in self.accounts:
            account_info = self.accounts[account_number]
            print("Account Holder Name:", account_info['name'])
            print("Account Balance:", account_info['balance'])
        else:
            print("Account not found.")
bank = Bank()
# Creating an account for Aiswarya
account_number = "123456"
name = "Aiswarya"
initial_balance = 50000
bank.create_account(account_number, name, initial_balance)
# Deposit amount
amount_to_deposit = 10000
bank.deposit(account_number, amount_to_deposit)
# Withdraw amount
amount_to_withdraw = 4000
bank.withdraw(account_number, amount_to_withdraw)
# Display account details
print("\nAccount Details:")
bank.account_details(account_number)


