import sqlite3
from settings import DB_NAME
from queries import (create_user_table, create_movie_table,
                     insert_initial_movies_in_movie_table,
                     create_projection_table,
                     insert_initial_projections_in_projection_table,
                     create_reservation_table,
                     insert_initial_user_in_user_table,
                     insert_initial_reservations_in_reservation_table,
                     insert_user_in_user_table)


def create_tables(cursor):
    cursor.execute(create_user_table)
    cursor.execute(create_movie_table)
    cursor.execute(create_projection_table)
    cursor.execute(create_reservation_table)


def insert_initial_data_into_tables(cursor):
    cursor.execute(insert_initial_user_in_user_table)
    cursor.execute(insert_initial_movies_in_movie_table)
    cursor.execute(insert_initial_projections_in_projection_table)
    cursor.execute(insert_initial_reservations_in_reservation_table)


def setup_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    create_tables(cursor)
    try:
        insert_initial_data_into_tables(cursor)
    except sqlite3.IntegrityError:
        pass
    # cursor.execute(create_user_table)
    # cursor.execute(insert_user_in_user_table, (SU_NAME, None, SU_PASS, 1))
    connection.commit()
    connection.close()


if __name__ == '__main__':
    setup_database()
