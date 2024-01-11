import pytest
from app.banco import ContaBancaria

class TestBanco:
    # deposit positive value increases account balance and prints success message
    def test_deposit_positive_value(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.deposito(200.0)
        assert conta.saldo == 1200.0
    
    # deposit zero value does not change account balance and prints error message
    def test_deposit_zero_value(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.deposito(0.0)
        assert conta.saldo == 1000.0

    # deposit negative value prints error message
    def test_deposit_negative_value(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.deposito(-200.0)
        assert conta.saldo == 1000.0

    # withdraw positive value decreases account balance and prints success message
    def test_withdraw_positive_value(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.saque(200.0)
        assert conta.saldo == 800.0

    # withdraw zero value does not change account balance and prints error message
    def test_withdraw_zero_value(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.saque(0.0)
        assert conta.saldo == 1000.0

    # withdraw negative value prints error message
    def test_withdraw_negative_value(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.saque(-200.0)
        assert conta.saldo == 1000.0

    # withdraw value greater than account balance prints error message
    def test_withdraw_greater_than_balance(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.saque(1200.0)
        assert conta.saldo == 1000.0

    # transfer positive value from one account to another decreases sender's balance and increases receiver's balance, and prints success message
    def test_transfer_positive_value(self):
        conta1 = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta2 = ContaBancaria(numero_conta=2, titular="Maria", saldo=500.0)
        conta1.transferencia(conta2, 200.0)
        assert conta1.saldo == 800.0
        assert conta2.saldo == 700.0

    # transfer negative value prints error message
    def test_transfer_negative_value(self):
        conta1 = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta2 = ContaBancaria(numero_conta=2, titular="Maria", saldo=500.0)
        conta1.transferencia(conta2, -200.0)
        assert conta1.saldo == 1000.0
        assert conta2.saldo == 500.0

    # transfer value greater than receiver's balance prints error message
    def test_transfer_greater_than_balance(self):
        conta1 = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta2 = ContaBancaria(numero_conta=2, titular="Maria", saldo=500.0)
        conta1.transferencia(conta2, 1200.0)
        assert conta1.saldo == 1000.0
        assert conta2.saldo == 500.0

    # transfer to same account prints error message
    def test_transfer_to_same_account(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.transferencia(conta, 200.0)
        assert conta.saldo == 1000.0

    # transfer to non-existent account prints error message
    def test_transfer_to_non_existent_account(self):
        conta1 = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta2 = None
        conta1.transferencia(conta2, 200.0)
        assert conta1.saldo == 1000.0

    # transfer zero value does not change account balances and prints error message
    def test_transfer_zero_value(self):
        conta1 = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta2 = ContaBancaria(numero_conta=2, titular="Maria", saldo=500.0)

        conta1.transferencia(conta2, 0.0)

        assert conta1.saldo == 1000.0
        assert conta2.saldo == 500.0

    # transfer value greater than sender's balance prints error message
    def test_transfer_value_greater_than_sender_balance(self):
        conta1 = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta2 = ContaBancaria(numero_conta=2, titular="Maria", saldo=500.0)
    
        conta1.transferencia(conta2, 1500.0)
        assert conta1.saldo == 1000.0
        assert conta2.saldo == 500.0

    # print account statement shows account number and current balance
    def test_print_account_statement(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.ver_extrato()
        assert conta.numero_conta == 1
        assert conta.saldo == 1000.0

    # account can be created with zero balance
    def test_account_created_with_zero_balance(self):
        conta = ContaBancaria(numero_conta=1, titular="João")
        assert conta.saldo == 0.0

    # account balance can be negative
    def test_account_balance_can_be_negative(self):
        conta = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
        conta.saque(1500.0)
        assert conta.saldo == -500.0

    # account holder name can be empty
    def test_account_holder_name_can_be_empty(self):
        conta = ContaBancaria(numero_conta=1, titular="", saldo=1000.0)
        assert conta.titular == ""

    # account number can be negative
    def test_account_number_can_be_negative(self):
        conta = ContaBancaria(numero_conta=-1, titular="João", saldo=1000.0)
        assert conta.numero_conta == -1

    # account number can be zero
    def test_account_number_can_be_zero(self):
        conta = ContaBancaria(numero_conta=0, titular="João", saldo=1000.0)
        assert conta.numero_conta == 0