import pandas as pd
from .exceptions import AccountNotFoundException


class Ledger:

    def __init__(self, ledger_file_path):
        self._ledger_schema = {
            'date': 'datetime64[ns]',
            'sender': 'str',
            'receiver': 'str',
            'amount': 'float64'
        }

        self._load_ledger_file(ledger_file_path)
        self._set_ledger_schema()

    def _load_ledger_file(self, ledger_file_path):
        self._ledger_df = pd.read_csv(ledger_file_path,
                                      header=None,
                                      names=list(self._ledger_schema.keys()))

    def _set_ledger_schema(self):
        for column_name, column_type in self._ledger_schema.items():
            self._ledger_df[column_name] = self._ledger_df[column_name].astype(column_type)

    def _transactions(self, account, date=None):
        if account not in self._ledger_df.values:
            raise AccountNotFoundException(account)

        is_transaction_from_account = (self._ledger_df['sender'] == account) | (self._ledger_df['receiver'] == account)

        if date is None:
            return self._ledger_df.loc[is_transaction_from_account]

        is_transaction_until_date_from_account = is_transaction_from_account & (self._ledger_df['date'] <= date)
        return self._ledger_df.loc[is_transaction_until_date_from_account]

    def balance(self, account, date=None):
        def extract_transfer(row):
            return row['amount'] if row['receiver'] == account else -row['amount']

        transactions_df = self._transactions(account, date=date)
        return sum(transactions_df.apply(extract_transfer, axis=1, result_type='reduce'))
