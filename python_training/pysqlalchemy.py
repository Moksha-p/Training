


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy_utils import database_exists, create_database
# from local_settings import postgresql as settings
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String

# # Define the base class
# Base = declarative_base()

# # Define the User model
# class User(Base):
#     __tablename__ = 'users'  # Name of the table

#     id = Column(Integer, primary_key=True)  # Primary key column
#     username = Column(String, unique=True)    # Unique username column
#     email = Column(String, unique=True)       # Unique email column

#     def __repr__(self):
#         return f"<User(id={self.id}, username={self.username}, email={self.email})>"

# def get_engine(user, passwd, host, port, db):
#     url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
#     if not database_exists(url):
#         create_database(url)
#     engine = create_engine(url, pool_size=50, echo=False)
#     return engine

# def get_engine_from_settings():
#     keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
#     if not all(key in settings for key in keys):
#         raise Exception('Bad config file')

#     return get_engine(settings['pguser'],
#                       settings['pgpasswd'],
#                       settings['pghost'],
#                       settings['pgport'],
#                       settings['pgdb'])

# def get_session():
#     engine = get_engine_from_settings()
#     session = sessionmaker(bind=engine)()
#     return session

# # Create the engine and the session
# engine = get_engine(settings['pguser'],
#                     settings['pgpasswd'],
#                     settings['pghost'],
#                     settings['pgport'],
#                     settings['pgdb'])

# # Create all tables in the database
# Base.metadata.create_all(engine)

# # Now you can create a session and interact with the database
# session = get_session()

# # Optionally, add a user to the table
# new_user = User(username='testuser', email='test@example.com')
# session.add(new_user)
# session.commit()

# # Close the session
# session.close()
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy_utils import database_exists, create_database
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import func
# from local_settings import postgresql as settings

# # Define the base class
# Base = declarative_base()

# # Define the Product model
# class Product(Base):
#     __tablename__ = 'products'  # Name of the table

#     id = Column(Integer, primary_key=True)  # Primary key column
#     name = Column(String, nullable=False)   # Product name column
#     category = Column(String, nullable=False)  # Product category column
#     price = Column(Float, nullable=False)   # Product price column

#     def __repr__(self):
#         return f"<Product(id={self.id}, name={self.name}, category={self.category}, price={self.price})>"

# def get_engine(user, passwd, host, port, db):
#     url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
#     if not database_exists(url):
#         create_database(url)
#     engine = create_engine(url, pool_size=50, echo=False)
#     return engine

# def get_engine_from_settings():
#     keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
#     if not all(key in settings for key in keys):
#         raise Exception('Bad config file')

#     return get_engine(settings['pguser'],
#                       settings['pgpasswd'],
#                       settings['pghost'],
#                       settings['pgport'],
#                       settings['pgdb'])

# def get_session():
#     engine = get_engine_from_settings()
#     session = sessionmaker(bind=engine)()
#     return session

# # Create the engine and the session
# engine = get_engine(settings['pguser'],
#                     settings['pgpasswd'],
#                     settings['pghost'],
#                     settings['pgport'],
#                     settings['pgdb'])

# # Create all tables in the database
# Base.metadata.create_all(engine)

# # Now you can create a session and interact with the database
# session = get_session()

# # Insert sample data into the products table
# products_data = [
#     {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
#     {'name': 'Smartphone', 'category': 'Electronics', 'price': 700},
#     {'name': 'Table', 'category': 'Furniture', 'price': 150},
#     {'name': 'Chair', 'category': 'Furniture', 'price': 85}
# ]

# # Add sample data to the session
# for product_data in products_data:
#     new_product = Product(**product_data)
#     session.add(new_product)

# # Commit the changes
# session.commit()

# # Queries

# # Query 1: Retrieve all products in a specific category ('Electronics')
# category_to_search = 'Electronics'
# products_in_category = session.query(Product).filter(Product.category == category_to_search).all()
# print(f"Products in category '{category_to_search}': {products_in_category}")

# # Query 2: Retrieve products with a price above a certain threshold (e.g., price > 500)
# price_threshold = 500
# products_above_price = session.query(Product).filter(Product.price > price_threshold).all()
# print(f"Products with price greater than {price_threshold}: {products_above_price}")

# # Query 3: Retrieve the average price of products in each category
# average_price_per_category = session.query(Product.category, func.avg(Product.price)).group_by(Product.category).all()
# print("Average price of products in each category:")
# for category, avg_price in average_price_per_category:
#     print(f"Category: {category}, Average Price: {avg_price}")

# # Close the session
# session.close()


from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func, select
from local_settings import postgresql as settings
from functools import lru_cache

# Define the base class
Base = declarative_base()

# Task 1: Define the Product model
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, category={self.category}, price={self.price})>"

def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in settings for key in keys):
        raise Exception('Bad config file')

    return get_engine(settings['pguser'],
                      settings['pgpasswd'],
                      settings['pghost'],
                      settings['pgport'],
                      settings['pgdb'])

def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session

# Create the engine and the session
engine = get_engine(settings['pguser'],
                    settings['pgpasswd'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])

Base.metadata.create_all(engine)

session = get_session()

# Task 1: Insert sample data into the products table
products_data = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
    {'name': 'Smartphone', 'category': 'Electronics', 'price': 700},
    {'name': 'Table', 'category': 'Furniture', 'price': 150},
    {'name': 'Chair', 'category': 'Furniture', 'price': 85}
]

for product_data in products_data:
    new_product = Product(**product_data)
    session.add(new_product)

session.commit()

# Task 1: Queries

# Query 1: Retrieve all products in a specific category ('Electronics')
category_to_search = 'Electronics'
products_in_category = session.query(Product).filter(Product.category == category_to_search).all()
print(f"Products in category '{category_to_search}': {products_in_category}")

# Query 2: Retrieve products with a price above a certain threshold (e.g., price > 500)
price_threshold = 500
products_above_price = session.query(Product).filter(Product.price > price_threshold).all()
print(f"Products with price greater than {price_threshold}: {products_above_price}")

# Query 3: Retrieve the average price of products in each category
average_price_per_category = session.query(Product.category, func.avg(Product.price)).group_by(Product.category).all()
print("Average price of products in each category:")
for category, avg_price in average_price_per_category:
    print(f"Category: {category}, Average Price: {avg_price}")

# Close the session
session.close()

# -----------------------------------------------
# Task 2: Add product caching using LRU Cache
# -----------------------------------------------

# Cache function to retrieve product details by name
@lru_cache(maxsize=128)
def get_product_by_name(product_name):
    session = get_session()
    query = session.query(Product).filter(Product.name == product_name).first()
    session.close()
    return query

# Example use of the cached function
product_name_to_search = 'Laptop'
product_details = get_product_by_name(product_name_to_search)
print(f"Product details (from cache) for '{product_name_to_search}': {product_details}")
print(get_product_by_name.cache_info())  # Show cache statistics

# -----------------------------------------------
# Task 3: Relationships and Caching
# -----------------------------------------------

# Define the Author model
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name})>"

# Define the Book model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, author_id={self.author_id})>"

# Create tables
Base.metadata.create_all(engine)

# Insert sample data for authors and books
authors_data = [{'name': 'J.K. Rowling'}, {'name': 'George R.R. Martin'}]
books_data = [
    {'title': 'Harry Potter and the Philosopher\'s Stone', 'author_id': 1},
    {'title': 'Harry Potter and the Chamber of Secrets', 'author_id': 1},
    {'title': 'A Game of Thrones', 'author_id': 2},
    {'title': 'A Clash of Kings', 'author_id': 2}
]

session.bulk_insert_mappings(Author, authors_data)
session.bulk_insert_mappings(Book, books_data)
session.commit()

# Caching function to retrieve author and their books
@lru_cache(maxsize=128)
def get_author_and_books(author_name):
    session = get_session()
    query = select(Author.name, Book.title).join(Book).where(Author.name == author_name)
    result = session.execute(query).fetchall()
    session.close()
    
    if result:
        author_name = result[0][0]
        books = [row[1] for row in result]
        return author_name, books
    return None

# Example test case for Task 3
author, books = get_author_and_books('George R.R. Martin')
print(f"Author: {author}, Books: {books}")
print(get_author_and_books.cache_info())  # Cache statistics

# -----------------------------------------------
# Task 4: Caching Complex Queries
# -----------------------------------------------

# Insert more sample data into the products table
more_products_data = [
    {'name': 'Desk', 'category': 'Furniture', 'price': 200},
    {'name': 'Monitor', 'category': 'Electronics', 'price': 300},
    {'name': 'Headphones', 'category': 'Electronics', 'price': 150},
    {'name': 'Lamp', 'category': 'Furniture', 'price': 50}
]

session.bulk_insert_mappings(Product, more_products_data)
session.commit()

# Function to retrieve the top 3 most expensive products in each category
@lru_cache(maxsize=128)
def get_top_expensive_products():
    session = get_session()
    query = select(Product.category, Product.name, Product.price).order_by(Product.category, Product.price.desc())
    result = session.execute(query).fetchall()
    session.close()

    products_by_category = {}
    for category, name, price in result:
        if category not in products_by_category:
            products_by_category[category] = []
        if len(products_by_category[category]) < 3:
            products_by_category[category].append((name, price))
    
    return products_by_category

# Example test case for Task 4
top_expensive_products = get_top_expensive_products()
print("Top 3 most expensive products by category:")
for category, products in top_expensive_products.items():
    print(f"{category}: {products}")

print(get_top_expensive_products.cache_info())  # Cache statistics





