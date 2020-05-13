from models import User
from .database import Database


class UserGateway:
    def __init__(self):
        self.db = Database()

    def search_user_by_name(self, username):
        user = self.db.session.query(User).filter(User.username == username).first()
        self.db.commit()
        return user
        # self.db.cursor.execute(select_user_by_user_name, (username,))
        # selected_user_data = self.db.cursor.fetchone()
        # self.db.commit()
        # return selected_user_data

    def update_table_with_user_data(self, username, email, password, salt):
        self.db.add(User(username=username, email=email, password=password, salt=salt))
        self.db.commit()


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

    def select_projections_for_given_movie_and_date(self, movie, date):
        if date == '':
            self.db.cursor.execute(select_all_projections_for_movie, (movie,))
        else:
            self.db.cursor.execute(select_all_projections_for_movie_and_date, (movie, date))
        projections = self.db.cursor.fetchall()
        self.db.commit()
        return projections
