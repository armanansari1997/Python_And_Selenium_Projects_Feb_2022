import pytest as pytest

from BankAccount import BankAccount


class TestBankAccount:
    @pytest.fixture
    def create_bank_account(self):
        return BankAccount(1000)

    def test_create_bank_account_with_valid(self):
        my_account = BankAccount(1000)  # Have Created the bank account with 1000 initial balance
        assert my_account.get_balance() == 1000

    def test_check_balance_with_invalid(self):
        my_account = BankAccount('Abc')
        assert my_account.get_balance() == 'Abd'

    def test_create_bank_account_with_zero(self):
        my_account = BankAccount(0)
        assert  my_account.get_balance() == 0

    def test_deposit_and_withdraw_balance(self, create_bank_account):
        # my_account = BankAccount(1000)
        create_bank_account.deposit(5000)
        assert create_bank_account.get_balance() == 6000
        create_bank_account.withdraw(2000)
        assert create_bank_account.get_balance() == 4000

    def test_fee_balance(self, create_bank_account):
        create_bank_account.withdraw(1001)
        assert create_bank_account.get_fees() == 5
        assert create_bank_account.get_balance() == -6
        create_bank_account.withdraw(100)
        assert create_bank_account.get_fees() == 10
        assert create_bank_account.get_balance() == -111

    def test_check_withdraw_limit(self, create_bank_account):
        create_bank_account.withdraw(100)
        create_bank_account.withdraw(100)
        create_bank_account.withdraw(100)
        create_bank_account.withdraw(100)
        create_bank_account.withdraw(100)
        assert create_bank_account.withdraw_count == 5
        # with pytest.raises(Exception, match='Withdraw limit exceeded'):
        #     create_bank_account.withdraw(100) ## We are expecting  Exception
        with pytest.raises(Exception) as exception:
            create_bank_account.withdraw(100)

    @pytest.mark.one
    def test_for_group(self):
        print()

    def test_create_bank_account(self):
        print("Test for create bank account")

    def test_check_balance(self):
        print("Test for check balance")
