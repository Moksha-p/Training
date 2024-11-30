from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:ashilshah@localhost/postgres'

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)


Base.metadata.create_all(engine)


#sample data
products_data = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
    {'name': 'Smartphone', 'category': 'Electronics', 'price': 700},
    {'name': 'Table', 'category': 'Furniture', 'price': 150},
    {'name': 'Chair', 'category': 'Furniture', 'price': 85},
]


for data in products_data:
    session.add(Product(**data))
session.commit()

#Retrieve all products in 'Electronics' category
electronics_products = session.query(Product.name, Product.category, Product.price).filter(
    Product.category == 'Electronics'
).all()

#Retrieve products with price > 500
expensive_products = session.query(Product.name, Product.category, Product.price).filter(
    Product.price > 500
).all()

#Retrieve average price of products in each category
average_prices = session.query(
    Product.category, func.avg(Product.price)
).group_by(Product.category).all()

print("Query 1: Products in 'Electronics' category:", electronics_products)
print("Query 2: Products with price > 500:", expensive_products)
print("Query 3: Average price by category:", average_prices)


from functools import lru_cache
import time

@lru_cache(maxsize=128)
def get_product_by_id(product_id):
    time.sleep(2)
    return session.query(Product.id, Product.name, Product.category, Product.price).filter(Product.id == product_id).first()

print(get_product_by_id(1))
print(get_product_by_id(1))
print(get_product_by_id.cache_info())

@lru_cache(maxsize=128)
def get_top_3_expensive_products_per_category():
    subquery = session.query(
        Product.category,
        Product.name,
        Product.price
    ).order_by(Product.category, Product.price.desc()).subquery()

    categories = session.query(subquery.c.category).distinct()
    result = []
    for category in categories:
        top_products = session.query(subquery.c.name, subquery.c.price).filter(subquery.c.category == category[0]).limit(3).all()
        result.append((category[0], top_products))
    return result

# Test Query
print(get_top_3_expensive_products_per_category())
