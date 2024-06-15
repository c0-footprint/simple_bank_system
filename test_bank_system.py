import unittest
from bank_system import BankSystem, BankAccount


class TestBankSystem(unittest.TestCase):

    def setUp(self):
        self.bank = BankSystem()

    def test_create_account(self):
        self.bank.reset_db(path='test_create_account.csv')
        self.assertTrue(self.bank.create_account('Alice', 1000))
        self.assertEqual(self.bank.get_account('Alice').balance, 1000)
        self.assertFalse(self.bank.create_account('Alice'))  # Duplicate account

    def test_get_account(self):
        self.bank.reset_db(path='test_get_account.csv')
        self.bank.create_account('Bob', 500)
        self.assertIsNotNone(self.bank.get_account('Bob'))
        self.assertIsNone(self.bank.get_account('Charlie'))  # Non-existent account

    def test_deposit(self):
        self.bank.reset_db(path='test_deposit.csv')
        self.bank.create_account('Alice', 1000)
        self.assertTrue(self.bank.deposit('Alice', 200))
        self.assertEqual(self.bank.get_account('Alice').balance, 1200)
        self.assertFalse(self.bank.deposit('Bob', 100))  # Account not created

    def test_withdraw(self):
        self.bank.reset_db(path='test_withdraw.csv')
        self.bank.create_account('Bob', 500)
        self.assertTrue(self.bank.withdraw('Bob', 100))
        self.assertEqual(self.bank.get_account('Bob').balance, 400)
        self.assertFalse(self.bank.withdraw('Alice', 100))  # Account not created
        self.assertFalse(self.bank.withdraw('Bob', 600))  # Insufficient funds

    def test_transfer(self):
        self.bank.reset_db(path='test_transfer.csv')
        self.bank.create_account('Alice', 1000)
        self.bank.create_account('Bob', 500)
        self.assertTrue(self.bank.transfer('Alice', 'Bob', 300))
        self.assertEqual(self.bank.get_account('Alice').balance, 700)
        self.assertEqual(self.bank.get_account('Bob').balance, 800)
        self.assertFalse(self.bank.transfer('Charlie', 'Bob', 100))  # Source not found
        self.assertFalse(self.bank.transfer('Alice', 'Bob', 1100))  # Insufficient funds


if __name__ == '__main__':
    unittest.main()
