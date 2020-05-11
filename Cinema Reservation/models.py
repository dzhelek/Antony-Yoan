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
        if not '@' in parseaddr(email)[1]:
            raise ValueError('invalid email address')

    @staticmethod
    def validate_password(password):
        if len(password) > 7:
            has_capital_letter = compile('[A-Z]')
            has_special_symbol = compile(r'[\W\S\D]')

            if not match(has_capital_letter, password):
                raise ValueError('password must contain a capital letter')

            if not match(has_special_symbol, password):
                raise ValueError('password must contain a special symbol')
        else:
            raise ValueError('password must be min 8 characters long')

    def __str__(self):
        return f'{self.id} | {self.username} | {self.email} | {self.password}'


class MovieModel:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating


class ProjectionModel:
    def __init__(self, id, movie_id, type, date, time):
        self.id = id
        self.movie_id = movie_id
        self.type = type
        self.date = date
        self.time = time
