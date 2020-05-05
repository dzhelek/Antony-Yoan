from os.path import exists

import gateway
from settings import DB_NAME, SU_NAME, SU_PASS


def build():
    print(f'''Database '{DB_NAME}' not detected!
Creating database...''')
    gateway.create_db()
    print(f'''
super user username: {SU_NAME}
super user password: {SU_PASS}''')


def start():
    pass


if __name__ == '__main__':
    if not exists(DB_NAME):
        build()
    start()
