import unittest
from app import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1000, "1234")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.assertTrue(self.account.deposit(500))
        self.assertEqual(self.account.get_balance(), 1500)
        self.assertFalse(self.account.deposit(-100))

    def test_withdraw(self):
        self.assertFalse(self.account.withdraw(2000))
        self.assertTrue(self.account.withdraw(800))
        self.assertEqual(self.account.get_balance(), 200)

    def test_display_info(self):
        self.assertEqual(self.account.display_info(), "Account 1234: Balance = $1000")

if __name__ == "__main__":
    unittest.main()