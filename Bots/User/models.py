from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from config import engine, session

user_table = declarative_base(engine)


class Users(user_table):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    def __init__(self, user_id):
        self.user_id = user_id
        session.add(self)
        session.commit()

