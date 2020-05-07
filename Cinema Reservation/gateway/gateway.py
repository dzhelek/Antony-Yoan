from models import UserModel
from database import Database
from queries import select_user_by_user_name, insert_user_in_user_table


class UserGateway:
    def __init__(self):
        # self.model = UserModel()
        self.db = Database()

    def search_user_by_name(self, username):
        self.db.cursor.execute(select_user_by_user_name, (username,))
        selected_user_data = self.db.cursor.fetchone()
        self.db.commit()
        return selected_user_data

    def update_table_with_user_data(self, username, email, password):
        self.db.cursor.execute(insert_user_in_user_table, (username, email, password))
        self.db.commit()
        # self.db.close()
        # self.db = Database()
        # self.model.validate(username, email, password)
        # self.db.cursor.execute()  # TODO: create user query

        # TODO: What whould I return?

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]