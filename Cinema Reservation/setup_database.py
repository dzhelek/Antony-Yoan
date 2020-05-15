from main.database import Database
from main.controllers import UserController, MovieController
from settings import SU_NAME, SU_PASS


def setup_database():
    db = Database()
    db.create()
    # db.insert()
    controller = UserController()
    controller.sign_user(username=SU_NAME, email=None,
                         password=SU_PASS, superuser=True)
    controller = MovieController()
    controller.add_movie('The Hunger Games: Catching Fire', 7.9)
    controller.add_movie('Wreck-It Ralph', 7.8)
    controller.add_movie('Her', 8.3)


if __name__ == '__main__':
    setup_database()
