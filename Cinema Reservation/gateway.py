from models import UserModel


class UserGateway:
    def __init__(self):
        # self.model = UserModel()
        self.db = Database()

    def log(self, username, password):
        pass

    def create(self, * ,username, email, password):
        self.model.validate(username, email, password)
        self.db.cursor.execute()  # TODO: create user query

        # TODO: What whould I return?

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]