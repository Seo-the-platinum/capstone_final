from sqlalchemy import (Column, String, Integer, create_engine,
 ForeignKey, DateTime)
from flask_sqlalchemy import SQLAlchemy
import json
import os
'''
database_path = 'postgresql://postgres:seoisoe5i73@localhost:5432/capstonedb'
'''
database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

#-----Models----

class Star(db.Model):
        __tablename__ = 'star'
        id = Column(Integer, primary_key=True)
        actor_id = Column(Integer,
        ForeignKey('actor.id'),nullable=False)
        movie_id = Column(Integer,
        ForeignKey('movie.id'), nullable=False)

        def __init__(self, actor_id, movie_id):
            self.actor_id = actor_id
            self.movie_id = movie_id

        def insert(self):
            db.session.add(self)
            db.session.commit()

        def delete(self):
            db.session.delete(self)
            db.session.commit()

        def update():
            db.session.commit()

        def format(self):
            return {
                'id': self.id,
                'actor_id': self.actor_id,
                'movie_id': self.movie_id,
            }

#class declaration and name it Movie. Pass the class
# the SQLAlchemy.model function to build our model
class Movie(db.Model):
        #name name table here and always use lowercase
        # if you use a capital letter, you will have to use
        # double quotes when running sql commands to access db.
        #its easier to just always use lowercase
        #double undscore is used to protect the tablename
        # var from being changed or mangled if we extend the class
        # to another model.
        __tablename__= 'movie'
        #create attributes here
        id=Column(Integer, primary_key=True)
        release_date=Column(DateTime)
        title=Column(String)
        stars = db.relationship('Star', cascade="all,delete",
        backref=db.backref('movie'), lazy='joined')
        #when a movie will be created, the init function
        # will be called and values passed as parameters will be
        # set as attribute vaules when the row is constructed
        #I.E  Movie('01/01/10', 'theres something about mary')
        #the values will be set when the row is constructed
        def __init__(self, release_date, title):
            self.release_date = release_date
            self.title = title
        #create an insert function to handle adding rows to
        # the table and commiting them. use Movie.add() and
        # movie.commit(). The insert, update, delete, and format
        # functions are used organize and make commiting to the db
        # shorter and neater
        def insert(self):
            db.session.add(self)
            db.session.commit()

        #commites updates for row
        def update(self):
            db.session.commit()

        #deletes and commits for row
        def delete(self):
            db.session.delete(self)
            db.session.commit()

        # find out more and add to comment on format func
        def format(self):
            return {
                'id': self.id,
                'release_date': self.release_date,
                'title': self.title
            }
class Actor(db.Model):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key = True)
    age = Column(Integer)
    gender = Column(String)
    name = Column(String)
    movies = db.relationship('Star', cascade="all,delete",
    backref=db.backref('actor'), lazy='joined')

    def __init__(self, age, gender, name):
      self.age = age
      self.gender = gender
      self.name = name

    def insert(self):
      db.session.add(self)
      db.session.commit()

    def update(self):
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()

    def format(self):
      return {
        'id': self.id,
        'age': self.age,
        'gender': self.gender,
        'name': self.name
      }
