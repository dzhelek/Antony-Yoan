import sqlite3
from settings import DB_NAME
from queries import create_user_table


def setup_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(create_user_table)
    connection.commit()
    connection.close()
