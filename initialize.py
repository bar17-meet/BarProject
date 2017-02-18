from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context


Base = declarative_base()


from databaseuser import User, Song
engine = create_engine('sqlite:///BarProject.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

a = Song()
session.add(a)
session.commit()
ido = User(firstname = "Ido", 
	password="ihatemyself",
	lastname="Wiernik",
	email="killme@fuck.com",
	birthdate = 5/2/3,
	country="depressionland",
	favmusic="emo",
	mysongs=a.id)
