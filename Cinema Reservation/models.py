from email.utils import parseaddr
from re import compile, match


class UserModel:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def validate_email(email):
        if '@' in parseaddr(email)[1]:
            return True
        else:
            return False

    @staticmethod
    def validate_password(password):
        if len(password) > 7:
            has_capital_letter = compile('[A-Z]')
            has_special_symbol = compile(r'[\W\S\D]')

            if match(has_capital_letter, password) and\
               match(has_special_symbol, password):
                return True
        return False

    def __str__(self):
        return f'{self.id} | {self.username} | {self.email} | {self.password}'