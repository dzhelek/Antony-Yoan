from main.database import Database


def setup_database():
    db = Database()
    db.create()
    # db.insert()


if __name__ == '__main__':
    setup_database()
