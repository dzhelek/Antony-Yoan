from gateway.gateway import UserGateway, MovieGateway
from views_constants import INVALID_CHOICE_RETURNED_VALUE, CHOICE_FOR_LOGIN_IN_CHOOSE_LOGIN_OR_SIGNUP, CHOICE_FOR_SIGNUP_IN_CHOOSE_LOGIN_OR_SIGNUP
from models import UserModel, MovieModel

class UserController:
    def __init__(self):
        self.gateway = UserGateway()

    def log_user(self, username, password):
        user_data = self.gateway.search_user_by_name(username)
        if user_data is not None:
            if password == user_data[3]:
                return UserModel(user_data[0], user_data[1], user_data[2], user_data[3])
        raise ValueError('Invalid username or password')  

    def sign_user(self, username, email, password):
        self.gateway.update_table_with_user_data(username, email, password)

    def select_user_by_username(self, username, password):
        return self.gateway.search_user_by_name(username)


class MovieController:
    def __init__(self):
        self.gateway = MovieGateway()

    def show_movies(self):
        movies_selected = self.gateway.select_all_movies()
        movies = []
        for movie in movies_selected:
            id = movie[0]
            name = movie[1]
            rating = movie[2]
            movies.append(MovieModel(id, name, rating))
        return movies
