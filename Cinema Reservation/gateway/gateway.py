from models import UserModel
from database import Database
from queries import select_user_by_user_name, insert_user_in_user_table, select_all_movies_in_movie_table, select_all_projections_for_movie, select_all_projections_for_movie_and_date


class UserGateway:
    def __init__(self):
        # self.model = UserModel()
        self.db = Database()

    def search_user_by_name(self, username):
        self.db.cursor.execute(select_user_by_user_name, (username,))
        selected_user_data = self.db.cursor.fetchone()
        self.db.commit()
        return selected_user_data

    def update_table_with_user_data(self, username, email, password, salt):
        self.db.cursor.execute(insert_user_in_user_table,
                               (username, email, password, salt, 0))
        self.db.commit()
        # self.db.close()
        # self.db = Database()
        # self.model.validate(username, email, password)
        # self.db.cursor.execute()  # TODO: create user query

        # TODO: What whould I return?

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]


class MovieGateway:
    def __init__(self):
        self.db = Database()

    def select_all_movies(self):
        self.db.cursor.execute(select_all_movies_in_movie_table)
        selected_movies = self.db.cursor.fetchall()
        self.db.commit()
        return selected_movies


class ProjectionGateway:
    def __init__(self):
        self.db = Database()

    def select_projections_for_given_movie_and_date(self, movie, date=None):
        if date is None:
            self.db.cursor.execute(select_all_projections_for_movie, (movie,))
        else:
            self.db.cursor.execute(select_all_projections_for_movie_and_date, (movie, date))
        projections = self.db.cursor.fetchall()
        self.db.commit()
        return projections
