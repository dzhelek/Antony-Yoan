create_user_table = '''CREATE TABLE IF NOT EXISTS user(
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       username VARCHAR(20) UNIQUE,
                       email VARCHAR(20) UNIQUE,
                       password VARCHAR(20)
                       )
'''
create_movie_table = '''CREATE TABLE IF NOT EXISTS movie(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50) UNIQUE,
                        rating REAL
                        )
'''

insert_initial_movies_in_movie_table = '''INSERT INTO movie (name, rating)
                                          VALUES ('The Hunger Games: Catching Fire', 7.9),
                                                 ('Wreck-It Ralph', 7.8),
                                                 ('Her', 8.3)
'''


select_user_by_user_name = 'SELECT * FROM user WHERE username = ?'
insert_user_in_user_table = 'INSERT INTO user (username, email, password) VALUES (?, ?, ?)'

select_all_movies_in_movie_table = 'SELECT * FROM movie ORDER BY rating DESC'
