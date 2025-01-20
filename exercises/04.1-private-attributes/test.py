import pytest
from io import StringIO
from unittest.mock import patch


@pytest.mark.it("Should ensure BankAccount class is defined correctly")
def test_bank_account_class_exists():
    import app 
    # Verificar que la clase BankAccount exista en el módulo app
    assert hasattr(app, "BankAccount"), "BankAccount class is not defined in app.py"


@pytest.mark.it("Should ensure BankAccount has all required methods")
def test_bank_account_methods():
    import app 
    account = app.BankAccount(1000, "1234")

    # Comprobar que los métodos existan en la clase
    assert hasattr(account, "deposit"), "Method 'deposit' is missing in BankAccount"
    assert hasattr(account, "withdraw"), "Method 'withdraw' is missing in BankAccount"
    assert hasattr(account, "get_balance"), "Method 'get_balance' is missing in BankAccount"
    assert hasattr(account, "display_info"), "Method 'display_info' is missing in BankAccount"

@pytest.mark.it("Should perform bank operations and display correct balance")
def test_bank_account_operations():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app  # Import the file that contains your main code
        import importlib
        importlib.reload(app)  
        # Crear la instancia de BankAccount
        account = app.BankAccount(1000, "1234")

        # Verificar saldo inicial
        assert account.get_balance() == 1000, "Initial balance should be 1000"

        # Depositar 500
        account.deposit(500)
        assert account.get_balance() == 1500, "Balance should be 1500 after deposit"

        # Intentar retirar 2000 (debería fallar por saldo insuficiente)
        account.withdraw(2000)
        assert account.get_balance() == 1500, "Balance should remain 1500 after failed withdrawal"

        # Retirar 800
        account.withdraw(800)
        assert account.get_balance() == 700, "Balance should be 700 after withdrawal"

        # Mostrar información de la cuenta
        account.display_info()
        output = mock_stdout.getvalue().strip()
        expected_output = "Account 1234: Balance = $700"
        assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"