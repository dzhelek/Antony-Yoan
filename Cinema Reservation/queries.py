create_user_table = '''CREATE TABLE IF NOT EXISTS user(
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       username VARCHAR(20) UNIQUE,
                       email VARCHAR(20) UNIQUE,
                       password VARCHAR(200),
                       salt VARCHAR(16),
                       superuser BOOL DEFAULT 0
                       );
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

create_reservation_table = '''CREATE TABLE IF NOT EXISTS reservation(
                             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                             user_id INTEGER NOT NULL,
                             projection_id INTEGER NOT NULL,
                             row INTEGER NOT NULL,
                             col INTEGER NOT NULL,
                             FOREIGN KEY(user_id) REFERENCES user(id),
                             FOREIGN KEY(projection_id) REFERENCES projection(id)
                             )
'''

insert_initial_user_in_user_table = '''INSERT INTO user (username, email, password) VALUES('user', 'user@abv.bg', '1234')'''

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

insert_initial_reservations_in_reservation_table = '''INSERT INTO reservation (user_id, projection_id, row, col)
                                                      VALUES (1, 1, 2, 1)                                                           
'''

select_user_by_user_name = 'SELECT * FROM user WHERE username = ?'
insert_user_in_user_table = '''INSERT INTO user
                               (username, email, password, salt, superuser)
                               VALUES (?, ?, ?, ?, ?)'''

select_all_movies_in_movie_table = 'SELECT * FROM movie ORDER BY rating DESC'

select_all_projections_for_movie = '''
  SELECT * FROM projection
  WHERE movie_id = (SELECT id FROM movie WHERE id = ?)
  ORDER BY date'''

select_all_projections_for_movie_and_date = '''
  SELECT * FROM projection
  WHERE movie_id = (SELECT id FROM movie WHERE id = ? AND date = ?)
  ORDER BY date'''
