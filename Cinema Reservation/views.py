from getpass import getpass
import subprocess

from controllers import UserController
from views_constants import *

from termcolor import colored


def clear_screen():
    subprocess.call('clear')


class UserViews:
    def __init__(self):
        self.controller = UserController()

    # def invalid_data_provided(self, message):
    #     print(message)

    def console_read_command_view(self):
        command = input('> ')
        return command

    def guest_user_help_view(self):
        print('\nlist of commands:\n')
        print('help')
        print('login')
        print('exit')
        print('signup')
        print()

    def error_view(self, error):
        print(error)

    def welcome_user(self, user):
        print(f'Hello, {user.username}')

    def choose_login_or_signup(self):
        print('Enter:')
        print(f'      {CHOICE_FOR_LOGIN_IN_CHOOSE_LOGIN_OR_SIGNUP} - login')
        print(f'      {CHOICE_FOR_SIGNUP_IN_CHOOSE_LOGIN_OR_SIGNUP} - signup')
        is_entering_system_successful = False
        while not is_entering_system_successful:
            choice = input(colored('Input: ', COLOR_IN_LOGIN_OR_SIGNUP))
            if choice == CHOICE_FOR_LOGIN_IN_CHOOSE_LOGIN_OR_SIGNUP:
                self.login()
                is_entering_system_successful = True
            elif choice == CHOICE_FOR_SIGNUP_IN_CHOOSE_LOGIN_OR_SIGNUP:
                self.signup()
                is_entering_system_successful = True
            else:
                print(colored('INVALID OPTION', INVALID_OPTION_TEXT_COLOR))

    def login(self):
        print('----- LOG IN -----')
        username = input(colored('Username: ', FIELD_COLOR_IN_LOG_IN))
        password = getpass(colored('Password: ', FIELD_COLOR_IN_LOG_IN))
        return (username, password)

    def signup(self):
        print('----- SIGH UP -----')
        username = input(colored('Username: ', FIELD_COLOR_IN_SIGN_UP))
        email = input(colored('Email: ', FIELD_COLOR_IN_SIGN_UP))
        password = getpass(colored('Password: ', FIELD_COLOR_IN_SIGN_UP))
        return (username, email, password)

    # def login(self):
    #     clear_screen()
    #     print('----- LOG IN -----')
    #     username = input(colored('Username: ', FIELD_COLOR_IN_LOG_IN))
    #     password = input(colored('Password: ', FIELD_COLOR_IN_LOG_IN))
    #     login_result = self.controller.log_user(username, password)
    #     does_want_to_signup = False
    #     while login_result != 'Correct':
    #         print(login_result)
    #         does_want_to_signup = input('You do not have a profile? Do you want to signup? y/n: ')
    #         if does_want_to_signup.lower() == 'y':
    #             does_want_to_signup = True
    #             break
    #         username = input(colored('Username: ', FIELD_COLOR_IN_LOG_IN))
    #         password = input(colored('Password: ', FIELD_COLOR_IN_LOG_IN))
    #         login_result = self.controller.log_user(username, password)

    #     if does_want_to_signup is True:
    #         self.signup()

    # def signup(self):
    #     clear_screen()
    #     print('----- SIGH UP -----')
    #     username = input(colored('Username: ', FIELD_COLOR_IN_SIGN_UP))
    #     email = input(colored('Email: ', FIELD_COLOR_IN_SIGN_UP))
    #     password = input(colored('Password: ', FIELD_COLOR_IN_SIGN_UP))
    #     signup_result = self.controller.sign_user(username, email, password)

        # self.controller.create_user(email=email, password=password)

    def show_movies(self, movies):
        for movie in movies:
            print(movie)

    def help(self):
        print('----- HELP -----')
        print('Available commands:\n')
        print(colored('show movies', COMMAND_COLOR_IN_HELP), ' - show all movies ordered by rating')
        print(colored('show movie projections <movie_id> [<date>]', COMMAND_COLOR_IN_HELP),
                      ' - show all projections of a given movie for the given date(optional)')
        print(colored('make reservation', COMMAND_COLOR_IN_HELP))
        print(colored('cancel reservation <name>', COMMAND_COLOR_IN_HELP))
        print(colored('exit', COMMAND_COLOR_IN_HELP))

    def exit(self, username='guest'):
        print(colored(f'Goodbye, {username}!', COLOR_IN_EXIT, attrs=['bold']))


if __name__ == '__main__':
    view = UserViews()
    view.exit('gosho')
