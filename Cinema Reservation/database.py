import pysqlite3

from settings import DB_NAME


class Database:
    def __init__(self):
        self.connection = pysqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()