from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:ashilshah@localhost/postgres'

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from functools import lru_cache
import time

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")

Base.metadata.create_all(engine)

#sample data
authors_data = [{'name': 'J.K. Rowling'}, {'name': 'George R.R. Martin'}]
books_data = [
    {'title': 'Harry Potter and the Philosopher\'s Stone', 'author_id': 1},
    {'title': 'Harry Potter and the Chamber of Secrets', 'author_id': 1},
    {'title': 'A Game of Thrones', 'author_id': 2},
    {'title': 'A Clash of Kings', 'author_id': 2}
]

for data in authors_data:
    session.add(Author(**data))
session.commit()

for data in books_data:
    session.add(Book(**data))
session.commit()

@lru_cache(maxsize=128)
def get_books_by_author(author_name):
    author = session.query(Author).filter(Author.name == author_name).first()
    return [(book.title,) for book in author.books]

@lru_cache(maxsize=128)
def get_author_with_books(author_name):
    author = session.query(Author).filter(Author.name == author_name).first()
    return (author.name, [(book.title,) for book in author.books])

# Test Queries
print(get_books_by_author('J.K. Rowling'))
print(get_author_with_books('George R.R. Martin'))

