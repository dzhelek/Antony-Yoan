create_user_table = '''CREATE TABLE IF NOT EXISTS user(
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       username VARCHAR(20) UNIQUE,
                       email VARCHAR(20) UNIQUE,
                       password VARCHAR(20)
                       )
'''
select_user_by_user_name = 'SELECT * FROM user WHERE username = ?'
insert_user_in_user_table = 'INSERT INTO user (username, email, password) VALUES (?, ?, ?)'

select_all_movies_in_movie_table = 'SELECT * FROM movie'
