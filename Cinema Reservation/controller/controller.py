from sqlite3 import connect


class Controller:
	def __init__(self):
		self.connection = connect()