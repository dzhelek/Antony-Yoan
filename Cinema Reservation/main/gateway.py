from models import User, Movie, Projection
from database import Database
from queries import select_user_by_user_name, insert_user_in_user_table, select_all_movies_in_movie_table, select_all_projections_for_movie, select_all_projections_for_movie_and_date


class UserGateway:
    def __init__(self):
        self.db = Database()

    def search_user_by_name(self, username):
        user = self.db.session.query(User).filter(User.username == username).first()
        self.db.commit()
        return user

    def update_table_with_user_data(self, username, email, password, salt):
        self.db.session.add(User(username=username, email=email, password=password, salt=salt))
        self.db.commit()


class MovieGateway:
    def __init__(self):
        self.db = Database()

    def select_all_movies(self):
        movies = self.db.session.query(Movie).all()
        self.db.commit()
        return movies


class ProjectionGateway:
    def __init__(self):
        self.db = Database()

    def select_projections_for_given_movie_and_date(self, movie, date):
        projections = []
        print(movie)
        if date == '':
            projections = self.db.session.query(Movie.projections).filter(Movie.id == movie).all()
        else:
            projections = self.db.session.query(Movie.projections).filter(Movie.id == movie, Movie.date == date).all()
        self.db.commit()
        return projections
