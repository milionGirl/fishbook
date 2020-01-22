from sqlalchemy import Column,String,Integer
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(20))
    binding = Column(String(20))
    publisher =Column(String(20))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate =Column(String(20))
    isbn = Column(String(20), nullable=False, unique=False)
    summary = Column(String(1000))
    image =Column(String(100))

    def sample(self):
        pass