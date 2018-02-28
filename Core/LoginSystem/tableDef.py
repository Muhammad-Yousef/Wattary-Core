"""""""Configuration Files"""""""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# ############################Classes############################### #

class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    # ----------------------------Constructor------------------------------------------#
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password


# create tables
engine = create_engine('sqlite:///Users.db', echo=True)
Base.metadata.create_all(engine)
