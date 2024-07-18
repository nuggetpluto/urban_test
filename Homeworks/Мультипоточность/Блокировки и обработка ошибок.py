import threading

class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            new_balance = self.balance + amount
            print(f"Deposited {amount}, new balance is {new_balance}")
            self.balance = new_balance

    def withdraw(self, amount):
        with self.lock:
            new_balance = self.balance - amount
            print(f"Withdrew {amount}, new balance is {new_balance}")
            self.balance = new_balance

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

if __name__ == "__main__":
    account = BankAccount()

    deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()
