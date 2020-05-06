from models import UserModel
from database import Database
from queries import select_user_by_user_name


class UserGateway:
    def __init__(self):
        # self.model = UserModel()
        self.db = Database()

    def search_user_by_name(self, username, password):
        self.db.cursor.execute(select_user_by_user_name, (username,))
        return self.db.cursor.fetchone()


    def update_table_with_user_data(self, username, email, password):
        print('Zapochva proces na vpisvane, no ne e dovurshen')
        # self.model.validate(username, email, password)
        # self.db.cursor.execute()  # TODO: create user query

        # TODO: What whould I return?

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]