from getpass import getpass
import subprocess

from views_constants import *

from tabulate import tabulate
from termcolor import colored


def clear_screen():
    subprocess.call('clear')


class UserViews:
    def console_read_command_view(self):
        command = input('> ')
        return command

    def guest_user_help_view(self):
        print('\nlist of commands:\n')
        print(colored('exit\nhelp\n', COLOR_IN_EXIT))
        print(colored('''login
signup''', COMMAND_COLOR_IN_HELP))

    def error_view(self, error):
        print(error)

    def welcome_user(self, user):
        print(f'Hello, {user.username}')

    def logged_user_help_view(self):
        print('\nlist of commands:\n')
        print(colored('exit\nhelp\n', COLOR_IN_EXIT))
        print(colored('''make reservation
show movie projections <movie_id> [<date>]
show movies''', COMMAND_COLOR_IN_HELP))

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

    def exit(self, username='guest'):
        print(colored(f'Goodbye, {username}!', COLOR_IN_EXIT, attrs=['bold']))


class MovieViews:
    def show_all_view(self, movies):
        table = []
        print()
        for movie in movies:
            table.append([colored(movie.id, ID_COLOR),
                          movie.name, movie.rating])
        print(tabulate(table,
                       headers=[colored('id', ID_COLOR), 'name', 'rating']))


class ProjectionViews:
    def choose_movie_and_date(self):
        movie = input(colored('Movie: ', 'blue'))
        date = input(colored('Date: ', 'blue'))
        return (movie, date)

    def show_all_projections(self, projections):
        print()
        if projections == []:
            print('No projections available')
        table = []
        for projection in projections:
            table.append([colored(projection.id, ID_COLOR),
                          projection.type, projection.date, projection.time])
            # print(projection.type + ' ' + projection.date + ' ' + projection.time)
        print(tabulate(table, headers=[colored('id', ID_COLOR),
                                       'type', 'date', 'time']))

if __name__ == '__main__':
    view = UserViews()
    view.exit('gosho')
