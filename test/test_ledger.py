import pytest
import numpy as np

from ledger import Ledger, date, AccountNotFoundException

test_ledger = Ledger('test/resources/test_ledger.csv')


def test_initialize_ledger():
    assert test_ledger._ledger_df.shape == (3, 4)
    assert list(test_ledger._ledger_df.columns) == ['date', 'sender', 'receiver', 'amount']
    assert list(test_ledger._ledger_df.dtypes) == [np.dtype('datetime64[ns]'),
                                                   np.dtype('O'),
                                                   np.dtype('O'),
                                                   np.dtype('float64')]


def test_latest_balance():
    assert test_ledger.balance('mary') == 25.0
    assert test_ledger.balance('john') == -145.0


def test_latest_balance_when_account_does_not_exist():
    with pytest.raises(AccountNotFoundException, match=r"account 'peter' not found"):
        test_ledger.balance('peter')


def test_specific_date_balance():
    assert test_ledger.balance('mary', date=date('2015-01-16')) == 125.0
    assert test_ledger.balance('john',  date=date('2015-01-16')) == -125.0


def test_specific_date_balance_when_account_does_not_exist():
    with pytest.raises(AccountNotFoundException, match=r"account 'peter' not found"):
        test_ledger.balance('peter', date=date('2015-01-16'))


def test_specific_date_balance_when_date_without_transactions():
    assert test_ledger.balance('mary', date=date('2000-01-01')) == 0.0
