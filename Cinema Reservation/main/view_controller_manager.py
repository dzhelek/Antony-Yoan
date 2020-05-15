# from sqlite3 import Error
from .controllers import UserController, MovieController, ProjectionController
from .models import User
from .views import (UserViews, MovieViews, ProjectionViews,
                   ReservationViews, system_input)
from sqlalchemy.exc import IntegrityError
import re

class ViewControllerManager:
    def __init__(self):
        self.user_views = UserViews()
        self.user_controllers = UserController()
        self.movie_views = MovieViews()
        self.movie_controllers = MovieController()
        self.projection_views = ProjectionViews()
        self.projection_controllers = ProjectionController()
        self.reservation_views = ReservationViews()

    def manage_entering_system_views_and_controllers(self):
        is_system_entered = False
        user_entered_system = None
        while not is_system_entered:
            command = self.user_views.console_read_command_view()
            if command == 'help':
                self.user_views.guest_user_help_view()
            elif command == 'login':
                user_entered_system = self.manage_login_view_and_controller()
            elif command == 'signup':
                user_entered_system = self.manage_signup_view_and_controller()
            elif command == 'exit':
                raise SystemExit
            else:
                print(f'\'{command}\' command not found')
            if user_entered_system is not None:
                is_system_entered = True

        return user_entered_system

    def manage_login_view_and_controller(self):
        login_data = self.user_views.login()
        username_entered = login_data[0]
        password_entered = login_data[1]
        try:
            return self.user_controllers.log_user(username_entered, password_entered)
        except ValueError as err:
            self.user_views.error_view(str(err))

    def show_movies(self):
        all_movies = self.movie_controllers.show_movies()
        self.movie_views.show_all_view(all_movies)

    def show_movie_projections(self, movie, date=''):
        projections = self.projection_controllers.show_projection(movie, date)
        self.projection_views.show_all_projections(projections)

    def manage_user_commands_views_and_controllers(self, user):
        self.user_views.welcome_user(user)
        while True:
            command = self.user_views.console_read_command_view()
            if command == 'help':
                self.user_views.logged_user_help_view()
            elif command == 'show movies':
                self.show_movies()
            elif command.startswith('show movie projections'):
                # entered_data = self.projection_views.choose_movie_and_date()
                entered_data =\
                    command.replace('show movie projections', '').split()
                movie = entered_data[0]
                if len(entered_data) == 2:
                    date = entered_data[1]
                else:
                    date = ''
                try:
                    self.show_movie_projections(movie, date)
                except Exception as e:
                    print(str(e))
            elif command == 'make reservation':
                system_input('number of seats')
                self.show_movies()
                movie = system_input('movie')
                self.show_movie_projections(movie)
                projection = system_input('projection')

            elif command == 'exit':
                raise SystemExit
            else:
                print(f'\'{command}\' command not found')

    def manage_signup_view_and_controller(self):
        signup_data = self.user_views.signup()
        if isinstance(signup_data, ValueError):
            self.user_views.error_view(signup_data)
        else:
            username_entered = signup_data[0]
            email_entered = signup_data[1]
            password_entered = signup_data[2]
            try:
                self.user_controllers.sign_user(username_entered, email_entered, password_entered)
                user = self.user_controllers.select_user_by_username(username_entered, password_entered)
                return user
            # except Error as err:
            #     error_message_fields = str(err).split('.')
            #     message_to_print = f'User with this {error_message_fields[1]} already exists!'
            #     self.user_views.error_view(message_to_print)
            except ValueError as err:
                self.user_views.error_view(err)
            except IntegrityError as e:
                not_unique_constaint = re.search(': [a-z]+.[a-z]+', str(e)).group(0)
                error_message_fields = not_unique_constaint.split('.')
                message_to_print = f'User with this {error_message_fields[1]} already exists!'
                self.user_views.error_view(message_to_print)
                self.user_controllers.gateway.db.session.rollback()

    def release_resources(self):
        self.user_controllers.gateway.db.close()
        self.movie_controllers.gateway.db.close()
        self.projection_controllers.gateway.db.close()