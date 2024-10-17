# 1. Student Class
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __repr__(self):
        return f'name: "{self.name}", age: {self.age}, grades: {self.grades}'


# 2. Employee Class (from CSV file)
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f'Employee(name="{self.name}", position="{self.position}", salary={self.salary})'


# 3. BankAccount Class
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def __repr__(self):
        return f'account_number: "{self.account_number}", balance: {self.balance}'


# 4. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __repr__(self):
        return f'area: {self.area()}, perimeter: {self.perimeter()}'


# 5. Car Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f'make: "{self.make}", model: "{self.model}", year: {self.year}'


# 6. Customer Class (from JSON file)
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'Customer(name="{self.name}", email="{self.email}")'


# 7. Person Class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f'name: "{self.name}", age: {self.age}, address: "{self.address}"'


# 8. Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)

    def __repr__(self):
        return f'area: {self.area()}, circumference: {self.circumference()}'


# 9. Product Class (from CSV file)
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'Product(name="{self.name}", price={self.price}, quantity={self.quantity})'


# 10. Movie Class
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __repr__(self):
        return f'title: "{self.title}", director: "{self.director}", rating: {self.rating}'


# Test Cases
# 1. Student
student = Student(name="Alice", age=20, grades=[90, 85, 88])
print(student)

# 2. Employee
csv_data = [["John Doe", "Manager", 75000], ["Jane Smith", "Engineer", 80000]]
employees = [Employee(*data) for data in csv_data]
for emp in employees:
    print(emp)

# 3. Bank Account
account = BankAccount(account_number="12345678", initial_balance=1000)
print(account)

# 4. Rectangle
rectangle = Rectangle(length=5, width=3)
print(rectangle)

# 5. Car
car = Car(make="Toyota", model="Camry", year=2020)
print(car)

# 6. Customer
customer_data = {"name": "John Doe", "email": "john.doe@example.com"}
customer = Customer(name=customer_data["name"], email=customer_data["email"])
print(customer)

# 7. Person
person = Person(name="John Doe", age=30, address="123 Main St")
print(person)

# 8. Circle
circle = Circle(radius=4)
print(circle)

# 9. Product
csv_product_data = [["Laptop", 1000, 5], ["Phone", 500, 10]]
products = [Product(*data) for data in csv_product_data]
for product in products:
    print(product)

# 10. Movie
movie = Movie(title="Inception", director="Christopher Nolan", rating=8.8)
print(movie)
