#FONCTIONNE DBEAVER
# from sqlalchemy import create_engine, Column, String, Integer, Text
# from sqlalchemy.ext.declarative import declarative_base



# DATABASE_URL='postgresql://cool:Plasma20200@serveurcool.postgres.database.azure.com:5432/cooldb'

# engine = create_engine(DATABASE_URL)
# Base = declarative_base()

# class Film(Base):
#     __tablename__ = 'films'
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String)
#     original_title = Column(String)
#     score = Column(String)
#     genre = Column(Text)
#     year = Column(String)
#     duration = Column(Integer)
#     description = Column(Text)
#     actors = Column(Text)
#     director = Column(Text)

# Base.metadata.create_all(engine)
####FIN DBEAVER

from sqlalchemy import create_engine, Column, String, Integer, Text, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#à remplir depuis .env
DATABASE_URL = 'postgresql://adminname:adminpassword@NAMESERVER.postgres.database.azure.com:5432/dbname'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Table d'association pour les réalisateurs
realisation = Table('realisation', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('director_id', Integer, ForeignKey('directors.id'), primary_key=True)
)

# Table d'association pour les acteurs
role = Table('role', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True)
)

class Film(Base):
    __tablename__ = 'films'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    original_title = Column(String)
    score = Column(String)
    genre = Column(Text)
    year = Column(String)
    duration = Column(Integer)
    description = Column(Text)
    actors = relationship('Actor', secondary=role, back_populates='films')
    directors = relationship('Director', secondary=realisation, back_populates='films')

class Actor(Base):
    __tablename__ = 'actors'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    films = relationship('Film', secondary=role, back_populates='actors')

class Director(Base):
    __tablename__ = 'directors'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    films = relationship('Film', secondary=realisation, back_populates='directors')

Base.metadata.create_all(engine)
