# Simple Transaction Ledger

## Overview

A very simple transaction ledger library that loads a ledger file (CSV, without headers) and process
transactions to calculate account's balances.

## Installing the App

This project requires Python 3.

You might want to create your own [virtual environment](https://virtualenv.pypa.io/en/latest/) before installing this project.

From the project's directory, run the following command:

    pip install .

Now that the library has been installed, you may start a Python session and run some commands:

```bash
$ python
Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from ledger import Ledger
>>> my_ledger = Ledger('test/resources/test_ledger.csv')
```

The above commands parse an input ledger file and create a ledger object.

```bash
>>> my_ledger.balance('mary')
25.0
>>> my_ledger.balance('john')
-145.0
>>>
```

The above commands get the current balance for two accounts, which are identified by simple strings (e.g. "john", "mary")

We may also get the balance only up to a given input date:

```bash
>>> from ledger import date
>>> my_ledger.balance('mary', date=date('2015-01-16')) 
125.0
>>> my_ledger.balance('john', date=date('2015-01-16')) 
-125.0
>>> 
```

Note the `date()` constructor, which parses an input date string (currently only ISO is supported).

## Running Unit Tests

Install all the project dependencies in your Python environment:

    pip install -r requirements.txt
    pip install -r requirements-test.txt

Execute the following command to run unit tests:

    pytest -s -v

You should get an output similar to the following:

```editorconfig
=================================================== test session starts ===================================================
platform linux -- Python 3.8.2, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/franco/PycharmProjects/hypothesis/simple-transaction-ledger
collected 6 items                                                                                                         

test/test_ledger.py::test_initialize_ledger PASSED
test/test_ledger.py::test_latest_balance PASSED
test/test_ledger.py::test_latest_balance_when_account_does_not_exist PASSED
test/test_ledger.py::test_specific_date_balance PASSED
test/test_ledger.py::test_specific_date_balance_when_account_does_not_exist PASSED
test/test_ledger.py::test_specific_date_balance_when_date_without_transactions PASSED
```

## Coverage Reports

Generate the coverage reports:

    coverage run --source=ledger -m pytest

Show the coverage reports:

    coverage report

You should get an output similar to the following:

```editorconfig
Name                   Stmts   Miss  Cover
------------------------------------------
ledger/__init__.py         3      0   100%
ledger/exceptions.py       3      0   100%
ledger/ledger.py          25      0   100%
------------------------------------------
TOTAL                     31      0   100%
```
