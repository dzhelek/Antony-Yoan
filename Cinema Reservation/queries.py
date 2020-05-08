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

create_projection_table = '''CREATE TABLE IF NOT EXISTS projection(
                             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                             movie_id INTEGER NOT NULL,
                             type VARCHAR(3),
                             date DATE,
                             time TIME,
                             FOREIGN KEY(movie_id) REFERENCES movie(id)
                             )
'''

insert_initial_movies_in_movie_table = '''INSERT INTO movie (name, rating)
                                          VALUES ('The Hunger Games: Catching Fire', 7.9),
                                                 ('Wreck-It Ralph', 7.8),
                                                 ('Her', 8.3)
'''

insert_initial_projections_in_projection_table = '''INSERT INTO projection (movie_id, type, date, time)
                                                    VALUES (1, '3D', '2020-04-01', '19:10'),
                                                           (1, '2D', '2020-04-01', '19:00'),
                                                           (1, '4DX', '2020-04-02', '21:00'),
                                                           (3, '2D', '2020-04-05', '20:20'),
                                                           (2, '3D', '2020-04-02', '22:00'),
                                                           (2, '2D', '2020-04-02', '19:30')
'''

select_user_by_user_name = 'SELECT * FROM user WHERE username = ?'
insert_user_in_user_table = 'INSERT INTO user (username, email, password) VALUES (?, ?, ?)'

select_all_movies_in_movie_table = 'SELECT * FROM movie ORDER BY rating DESC'

select_all_projections_for_movie = 'SELECT * from projection where movie_id = (SELECT id from movie WHERE name = ?)'
