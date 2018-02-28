import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDef import *

engine = create_engine('sqlite:///Users.db')

# create a Session
Session = sessionmaker(bind=engine)
session = Session()
#
# user = User("admin", "password")
# session.add(user)
#
# user = User("python", "python")
# session.add(user)
#
# user = User("jumpiness", "python")
# session.add(user)
#
# # commit the record the database
# session.commit()
#
# session.commit()
