import os
from settings import DB_NAME
from setup_database import setup_database
from views import UserViews
from views import choose_login_or_signup, clear_screen


def welcome():
    print('----- WELCOME to our cinema reservation system! -----'.center(os.get_terminal_size().columns))


def start(self):
    clear_screen()
    welcome()
    views = UserViews()
    views.choose_login_or_signup()


if __name__ == '__main__':
    if not os.exists(DB_NAME):
        setup_database()
    start()
