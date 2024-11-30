from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from functools import lru_cache
import time

DATABASE_URL = 'postgresql://postgres:ashilshah@localhost/postgres'

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    is_deleted = Column(Integer, default=0)  # 0 = not deleted, 1 = deleted

Base.metadata.create_all(engine)

#sample data
users_data = [{'name': 'Alice', 'age': 31}, {'name': 'Bob', 'age': 28}]
for data in users_data:
    session.add(User(**data))
session.commit()

@lru_cache(maxsize=128)
def get_user_by_id(user_id):
    user = session.query(User).filter(User.id == user_id, User.is_deleted == 0).first()
    return (user.id, user.name, user.age) if user else None

def soft_delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.is_deleted = 1
        session.commit()

# Test Queries
soft_delete_user(2)
print(get_user_by_id(2))
print(get_user_by_id(1))