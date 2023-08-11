# Module 2, Lecture 3, Homework 2
# Develop a BankAccount class to represent a bank account. Add methods for withdrawing
# and depositing funds into the account. Use the magic method __str__ to display
# information about the account.

class BankAccount:
    def __init__(self, account_number, account_holder, balance, account_type,
                 interest_rate, opening_date, account_status, transaction_history,
                 withdrawal_limit, transaction_limit, currency, additional_services):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.opening_date = opening_date
        self.account_status = account_status
        self.transaction_history = transaction_history
        self.withdrawal_limit = withdrawal_limit
        self.transaction_limit = transaction_limit
        self.currency = currency
        self.additional_services = additional_services

    def lk_withdrawing(self, withdrawing_summa):
        if withdrawing_summa > self.withdrawal_limit:
            # raise ValueError("Invalid withdrawal amount: exceeds the withdrawal limit")
            return False
        if withdrawing_summa > self.balance:
            # raise ValueError("Invalid withdrawal amount: exceeds your balance")
            return False
        self.balance -= withdrawing_summa
        self.transaction_history.append(f"Withdrawal: {withdrawing_summa}")
        # return self.balance
        return True

    def lk_depositing(self, depositing_summa):
        if depositing_summa > self.transaction_limit:
            # raise ValueError("Invalid withdrawal amount: exceeds the transaction limit")
            return False
        self.balance += depositing_summa
        self.transaction_history.append(f"Deposit: {depositing_summa}")
        # return self.balance
        return True

    def __str__(self):
        return f"Account Number: {self.account_number}\n" \
               f"Account Holder: {self.account_holder}\n" \
               f"Balance: ${self.balance:.2f}\n" \
               f"Account Type: {self.account_type}\n" \
               f"Interest Rate: {self.interest_rate}\n" \
               f"Opening Date: {self.opening_date}\n" \
               f"Account Status: {self.account_status}\n" \
               f"Transaction History: {self.transaction_history}\n" \
               f"Withdrawal Limit: {self.withdrawal_limit}\n" \
               f"Transaction Limit: {self.transaction_limit}\n" \
               f"Currency: {self.currency}\n" \
               f"Additional Services: {self.additional_services}"


lk_account = BankAccount(
    account_number="1234567890",
    account_holder="Leonid Kadantsev",
    balance=1000.0,
    account_type="Savings",
    interest_rate=0.05,  # # The interest rate is set to 0.05 (5%).
    opening_date="2023-01-01",
    account_status="Active",
    transaction_history=[],
    withdrawal_limit=500.0,  # The maximum withdrawal limit is set to 500.0 USD.
    transaction_limit=1000.0,  # The maximum transaction limit is set to 1000.0 USD.
    currency="USD",
    additional_services=["Online Banking", "ATM Access"]
)

print(lk_account)
print(lk_account.balance)
lk_account.lk_withdrawing(333)
print(lk_account.balance)
lk_account.lk_depositing(444)
print(lk_account.balance)
print(lk_account.transaction_history)
lk_account.lk_withdrawing(334)
lk_account.lk_withdrawing(499)
lk_account.lk_withdrawing(500)
print(lk_account)
