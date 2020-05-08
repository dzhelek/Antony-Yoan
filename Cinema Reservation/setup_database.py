import sqlite3
from settings import DB_NAME
from queries import create_user_table, create_movie_table, insert_initial_movies_in_movie_table, create_projection_table, insert_initial_projections_in_projection_table


def setup_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(create_user_table)
    cursor.execute(create_movie_table)
    cursor.execute(insert_initial_movies_in_movie_table)
    cursor.execute(create_projection_table)
    cursor.execute(insert_initial_projections_in_projection_table)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    setup_database()
