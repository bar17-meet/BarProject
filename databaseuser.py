from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
#secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
import datetime

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email =  Column(String)
    birthdate = Column(Date)
    country = Column(String)
    favmusic = Column(String)
    mysongs = relationship("Song", back_populates="user")

class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    #user_id = Column(Integer,ForeignKey('user.id')
    #user = relationship("User", back_populates="mysongs")

engine = create_engine('sqlite:///BarProject.db')

date = datetime.date(year, month, day)

