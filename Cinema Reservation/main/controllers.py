from hashlib import sha512
from random import randint

from .gateway import UserGateway, MovieGateway, ProjectionGateway
from .models import User, Movie, Projection
from settings import HASHING_TIMES


class UserController:
    def __init__(self):
        self.gateway = UserGateway()

    def log_user(self, username, entered_password):
        user = self.gateway.search_user_by_name(username)
        if user is not None:
            entered_password = self.get_hash(entered_password, user.salt)
            if user.password == entered_password:
                return user
        else:
            raise ValueError('Invalid username or password')  

    def sign_user(self, username, email, password):
        password, salt = self.get_hashed_pass_and_salt(password)
        self.gateway.update_table_with_user_data(username, email,
                                                 password, salt)

    def select_user_by_username(self, username, password):
        return self.gateway.search_user_by_name(username)

    @staticmethod
    def get_hashed_pass_and_salt(password):
        salt = ''.join(chr(randint(32, 126)) for i in range(16))
        password += salt
        for i in range(HASHING_TIMES):
            password = sha512(password.encode()).hexdigest()

        return password, salt

    @staticmethod
    def get_hash(password, salt):
        password += salt
        for i in range(HASHING_TIMES):
            password = sha512(password.encode()).hexdigest()

        return password


class MovieController:
    def __init__(self):
        self.gateway = MovieGateway()

    def show_movies(self):
        # movies_selected = self.gateway.select_all_movies()
        # movies = []
        # for movie in movies_selected:
        #     id = movie[0]
        #     name = movie[1]
        #     rating = movie[2]
        #     movies.append(Movie(id, name, rating))
        # return movies
        return self.gateway.select_all_movies()


class ProjectionController:
    def __init__(self):
        self.gateway = ProjectionGateway()

    def show_projection(self, movie, date):
        projections_selected = self.gateway.select_projections_for_given_movie_and_date(movie, date)

        # projections = []
        # for projection in projections_selected:
        #     id = projection[0]
        #     movie_id = projection[1]
        #     type = projection[2]
        #     date = projection[3]
        #     time = projection[4]
        #     projections.append(ProjectionModel(id, movie_id, type, date, time))
        return projections_selected
