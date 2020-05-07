import sqlite3

connection = sqlite3.connect('cinema.db')
cursor = connection.cursor()
try:
	cursor.execute('insert into user (username, email, password) values (?, ?, ?)', ('user2', 'user2@abv.bg', '1234'))
except Exception as e:
	unique_error = str(e).split('.')
	print(unique_error[1])
print(cursor.fetchone())
connection.commit()
connection.close()