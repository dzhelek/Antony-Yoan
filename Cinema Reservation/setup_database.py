from main.database import Database
from main.controllers import UserController
from settings import SU_NAME, SU_PASS


def setup_database():
    db = Database()
    db.create()
    # db.insert()
    controller = UserController()
    controller.sign_user(username=SU_NAME, email=None,
                         password=SU_PASS, superuser=True)


if __name__ == '__main__':
    setup_database()
