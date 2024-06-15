import csv
import logging

DB_PATH = 'db.csv'


class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        logging.info('Amount must be greater than 0.')
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        elif amount <= 0:
            logging.info('Amount must be greater than 0.')
        elif amount > self.balance:
            logging.info('Balance is not enough.')
        return False

    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False


class BankSystem:
    def __init__(self, filename=DB_PATH):
        self.accounts = {}
        self.filename = filename
        self.load_from_csv()

    def create_db(self):
        with open(self.filename, 'w', newline='') as csvfile:
            pass

    def reset_db(self, path):
        self.filename = path
        with open(self.filename, 'w') as csvfile:
            pass

        self.load_from_csv()

    def create_account(self, name, starting_balance=0.0):
        if name in self.accounts:
            return False
        self.accounts[name] = BankAccount(name, starting_balance)
        self.save_to_csv()
        return True

    def get_account(self, name):
        return self.accounts.get(name)

    def save_to_csv(self):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'balance'])
            for account in self.accounts.values():
                writer.writerow([account.name, account.balance])

    def load_from_csv(self):
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['name']
                    balance = float(row['balance'])
                    self.accounts[name] = BankAccount(name, balance)
        except FileNotFoundError:
            pass

    def deposit(self, name, amount):
        account = self.get_account(name)
        if account and account.deposit(amount):
            self.save_to_csv()
            return True
        return False

    def withdraw(self, name, amount):
        account = self.get_account(name)
        if account and account.withdraw(amount):
            self.save_to_csv()
            return True
        return False

    def transfer(self, from_name, to_name, amount):
        from_account = self.get_account(from_name)
        to_account = self.get_account(to_name)
        if from_account and to_account and from_account.transfer(amount, to_account):
            self.save_to_csv()
            return True
        return False


# Example usage
if __name__ == "__main__":
    bank = BankSystem()
    bank.create_db()
    bank.create_account('Alice', 1000)
    bank.create_account('Bob', 500)
    bank.deposit('Alice', 200)
    bank.transfer('Alice', 'Bob', 300)
    bank.withdraw('Bob', 100)