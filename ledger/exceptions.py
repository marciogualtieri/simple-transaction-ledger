class AccountNotFoundException(Exception):
    def __init__(self, account):
        super(AccountNotFoundException, self).__init__(f'account \'{account}\' not found')
