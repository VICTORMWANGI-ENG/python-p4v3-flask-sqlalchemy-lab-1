from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
  __tablename__ = 'earthquake'
  id = db.Column(db.Integer, primary_key=True)
  magnitude = db.Column(db.Float)
  location = db.Column(db.String)
  year = db.Column(db.Integer)

def __repr__(self):
  return f"Earthquake(id={self.id}, magnitude={self.magnitude}, location={self.location}, year={self.year})"