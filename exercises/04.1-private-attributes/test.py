import pytest
from io import StringIO
from unittest.mock import patch


@pytest.mark.it("Should ensure BankAccount class is defined correctly")
def test_bank_account_class_exists():
    import app 
   
    assert hasattr(app, "BankAccount"), "BankAccount class is not defined in app.py"


@pytest.mark.it("Should ensure BankAccount has all required methods")
def test_bank_account_methods():
    import app 
    account = app.BankAccount(1000, "1234")


    assert hasattr(account, "deposit"), "Method 'deposit' is missing in BankAccount"
    assert hasattr(account, "withdraw"), "Method 'withdraw' is missing in BankAccount"
    assert hasattr(account, "get_balance"), "Method 'get_balance' is missing in BankAccount"
    assert hasattr(account, "display_info"), "Method 'display_info' is missing in BankAccount"

@pytest.mark.it("Should perform bank operations and display correct balance")
def test_bank_account_operations():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app 
        import importlib
        importlib.reload(app)  
       
        account = app.BankAccount(1000, "1234")

  
        assert account.get_balance() == 1000, "Initial balance should be 1000"

   
        account.deposit(500)
        assert account.get_balance() == 1500, "Balance should be 1500 after deposit"

    
        account.withdraw(2000)
        assert account.get_balance() == 1500, "Balance should remain 1500 after failed withdrawal"

    
        account.withdraw(800)
        assert account.get_balance() == 700, "Balance should be 700 after withdrawal"

     
        account.display_info()
        output = mock_stdout.getvalue().strip()
        expected_output = "Account 1234: Balance = $700"
        assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"