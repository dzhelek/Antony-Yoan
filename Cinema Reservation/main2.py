import os
from settings import DB_NAME
from setup_database import setup_database
from views import UserViews, clear_screen
from view_manager import UserViewControllerManager


def welcome():
    print('----- WELCOME to our cinema reservation system! -----'.center(os.get_terminal_size().columns))


def start():
    clear_screen()
    welcome()
    manager = UserViewControllerManager()
    user = manager.manage_entering_system_views_and_controllers()
    manager.manage_user_commands_views_and_controllers(user)
    manager.release_resources()


if __name__ == '__main__':
    # if not os.path.exists(DB_NAME):  #mislq che trqbva da se promeni, bazata danni e fail, koito trqbva da e suzdaden vinagi
    #     setup_database()
    start()