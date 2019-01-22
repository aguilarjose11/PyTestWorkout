# test_wallet.py

# to run tests, run command pytest.

import pytest
# python code to test out.
from wallet import Wallet, InsufficientAmount

'''
this is a decorator for pytest fixations to use code that is
repeated multiple times.
the fixtures can be seen by running pytest --fixtures .
they are useful for starting code at the begining, and they can return stuff!
'''
@pytest.fixture
def empty_wallet():
    ''' returns an empty wallet.'''
    return Wallet()

# same as above.
@pytest.fixture
def wallet():
    ''' returns a wallet with $20 in it.'''
    return Wallet(20)

'''
This is a testing class.
The class has to have Test at the begining of the class name.
'''
class Testwallet():
    #Testing...
    def test_default_initial_amount(self, empty_wallet):
        assert empty_wallet.balance == 0

    def test_setting_initial_amount(self, wallet):
        assert wallet.balance == 20

    def test_wallet_add_cash(self, wallet):
        wallet.add_cash(80)
        assert wallet.balance == 100

    def test_wallet_spend_cash(self, wallet):
        wallet.spend_cash(10)
        assert wallet.balance == 10

    def test_wallet_spend_cash_raises_exception_on_insufficient_amount(self, empty_wallet):
        with pytest.raises(InsufficientAmount):
            empty_wallet.spend_cash(100)

    '''
    This is a parametrized function.
    * It can only be used above the function that is to use them! *
    '''
    @pytest.mark.parametrize("earned, spent, expected", [
        (30, 10, 20),
        (20, 2, 18),
        (127, 127, 0)
    ])

    # this tests if multiple transactions actually work.
    def test_transactions(self, empty_wallet, earned, spent, expected):
        empty_wallet.add_cash(earned)
        empty_wallet.spend_cash(spent)
        assert empty_wallet.balance == expected
