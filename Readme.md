# Python Bank System
This Python code implements a simple bank system with account creation, deposit, withdrawal, and transfer functionalities. It leverages CSV files for data persistence and includes basic logging for informative messages.

## Features:

### Account Management:
Create new bank accounts with initial balances.
Retrieve existing accounts by name.
### Transactions:
Deposit funds into an account.
Withdraw funds from an account (with balance checks).
Transfer funds between accounts.
### Data Persistence:
Stores account information in a CSV file (db.csv by default).
Loads accounts from the CSV file upon initialization.

## Requirements:

Python 3 (tested with 3.x versions)

csv module (included in the standard library)

logging module (included in the standard library)
## Installation:

No external installation is required. Ensure you have Python 3 and its standard libraries available.

## Usage:
```Python
import bank_system

bank = bank_system.BankSystem()
bank.create_db()
bank.create_account('Alice', 1000)
bank.create_account('Bob', 500)
bank.deposit('Alice', 200)
bank.transfer('Alice', 'Bob', 300)
bank.withdraw('Bob', 100)
```

### Database Management:
```Python
bank.create_db()
bank.reset_db('new_db.csv')  # Specify a new file path if desired
```

## Logging:

The code uses the built-in logging module to provide informative messages about invalid transactions, such as insufficient balance or non-positive deposit/withdrawal amounts.

## Customization:

You can modify the DB_PATH constant to change the default CSV file path.