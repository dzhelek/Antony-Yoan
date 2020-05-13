from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Movie, Projection, Reservation, Base
from settings import DB_NAME, SU_NAME, SU_PASS


class Database:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{DB_NAME}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add(self, row):
        if isinstance(row, list):
            self.session.add_all(row)
        else:
            self.session.add(row)

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()

    def create(self):
        Base.metadata.create_all(self.engine)
