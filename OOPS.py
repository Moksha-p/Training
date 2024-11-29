class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f'name: "{self.name}", age: {self.age}, grades: {self.grades}'


student = Student(name="Alice", age=20, grades=[90, 85, 88])
print(student)  

import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'Employee(name="{self.name}", position="{self.position}", salary={self.salary})'

def parse_employees_from_csv(csv_content):
    employees = []
    for row in csv_content:
        employees.append(Employee(row[0], row[1], int(row[2])))
    return employees

csv_content = [["John Doe", "Manager", 75000], ["Jane Smith", "Engineer", 80000]]
employees = parse_employees_from_csv(csv_content)
for emp in employees:
    print(emp)


class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def __str__(self):
        return f'account_number: "{self.account_number}", balance: {self.balance}'

account = BankAccount(account_number="12345678", initial_balance=1000)
print(account) 


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(length=5, width=3)
print(f'area: {rectangle.area()}, perimeter: {rectangle.perimeter()}')

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f'make: "{self.make}", model: "{self.model}", year: {self.year}'

car = Car(make="Toyota", model="Camry", year=2020)
print(car)  

import json

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'Customer(name="{self.name}", email="{self.email}")'

def parse_customer_from_json(json_content):
    data = json.loads(json_content)
    return Customer(name=data["name"], email=data["email"])

json_content = '{"name": "John Doe", "email": "john.doe@example.com"}'
customer = parse_customer_from_json(json_content)
print(customer)  

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f'name: "{self.name}", age: {self.age}, address: "{self.address}"'
person = Person(name="John Doe", age=30, address="123 Main St")
print(person)  

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)

circle = Circle(radius=4)
print(f'area: {circle.area()}, circumference: {circle.circumference()}')


import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product(name="{self.name}", price={self.price}, quantity={self.quantity})'

def parse_products_from_csv(csv_content):
    products = []
    for row in csv_content:
        products.append(Product(name=row[0], price=int(row[1]), quantity=int(row[2])))
    return products

csv_content = [["Laptop", 1000, 5], ["Phone", 500, 10]]
products = parse_products_from_csv(csv_content)
for product in products:
    print(product)



class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __str__(self):
        return f'title: "{self.title}", director: "{self.director}", rating: {self.rating}'

movie = Movie(title="Inception", director="Christopher Nolan", rating=8.8)
print(movie)  


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

circle = Circle(radius=4)
square = Square(side=5)
print(f'Circle area: {circle.area()}, Circle perimeter: {circle.perimeter()}')
print(f'Square area: {square.area()}, Square perimeter: {square.perimeter()}')


class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def __str__(self):
        return f'Manager: {self.name}, Department: {self.department}'

class Engineer(Employee):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field

    def __str__(self):
        return f'Engineer: {self.name}, Field: {self.field}'

manager = Manager(name="John Doe", department="Sales")
engineer = Engineer(name="Jane Smith", field="Software")
print(manager)
print(engineer)

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

triangle = Triangle(base=5, height=3)
rectangle = Rectangle(length=4, width=2)
print(f'Triangle area: {triangle.area()}')
print(f'Rectangle area: {rectangle.area()}')

class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def __str__(self):
        return f'Bird: {self.name}, Can Fly: {self.can_fly}'

class Fish(Animal):
    def __init__(self, name, can_swim):
        super().__init__(name)
        self.can_swim = can_swim

    def __str__(self):
        return f'Fish: {self.name}, Can Swim: {self.can_swim}'

bird = Bird(name="Parrot", can_fly=True)
fish = Fish(name="Goldfish", can_swim=True)
print(bird)
print(fish)


class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def __str__(self):
        return f'Product(name="{self.name}", price={self.price}, quantity={self.quantity})'

def read_product_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        product = Product(data['name'], data['price'], data['quantity'])
        return product


product = Product("Laptop", 1000, 5)
print(product)

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f'{self.__class__.__name__}: {self.make} {self.model}'

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

car = Car(make="Toyota", model="Camry")
bike = Bike(make="Yamaha", model="MT-07")
print(car)
print(bike)

class User:
    def __init__(self, username, password):
        self._username = username 
        self._password = password 

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return "******"

    def __str__(self):
        return f'username: "{self.username}", password: "{self.password}"'

user = User(username="john_doe", password="secure123")
print(user) 

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def __str__(self):
        return f'name: "{self.name}", address: "{self.address}", books: {self.books}'

library = Library(name="City Library", address="123 Main St")
library.add_book("Book1")
library.add_book("Book2")
library.remove_book("Book1")
print(library)  

class House:
    def __init__(self, address, num_rooms, price):
        self.address = address
        self.num_rooms = num_rooms
        self.price = price

    def display_details(self):
        return f'address: "{self.address}", num_rooms: {self.num_rooms}, price: {self.price}'

house = House(address="456 Elm St", num_rooms=4, price=350000)
print(house.display_details())  


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discount(self, discount_rate):
        self.price -= self.price * discount_rate

    def display_details(self):
        print(f'title: "{self.title}", author: "{self.author}", price: {self.price:.2f}')

book = Book(title="Python 101", author="John Doe", price=29.99)
book.discount(0.1)
print(book)

class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating

    def __str__(self):
        return f'name: "{self.name}", cuisine_type: "{self.cuisine_type}", rating: {self.rating}'

restaurant = Restaurant(name="Sushi Place", cuisine_type="Japanese", rating=4.5)
restaurant.update_rating(4.8)
print(restaurant)  

class School:
    total_students = 0

    def __init__(self, name, students):
        self.name = name
        self.students = students
        School.total_students += students

    def enroll_students(self, count):
        self.students += count
        School.total_students += count

    def __str__(self):
        return f'name: "{self.name}", students: {self.students}, total_students: {School.total_students}'

school = School(name="Greenwood High", students=300)
school.enroll_students(50)
print(school)  

class Company:
    industry = "Technology"

    def __init__(self, name, num_employees):
        self.name = name
        self.num_employees = num_employees

    def update_employees(self, new_count):
        self.num_employees = new_count

    def __str__(self):
        return f'name: "{self.name}", num_employees: {self.num_employees}, industry: "{Company.industry}"'


company = Company(name="TechCorp", num_employees=200)
company.update_employees(220)
print(company)  

class MathUtils:
    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

print(MathUtils.is_prime(17)) 
print(MathUtils.is_prime(16))

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))  
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f'name: "{self.name}", salary: {self.salary}, programming_language: "{self.programming_language}"'

developer = Developer(name="Alice", salary=70000, programming_language="Python")
print(developer)  

class Appliance:
    def turn_on(self):
        return "Appliance is turned on"

class WashingMachine(Appliance):
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        return f"Washing Machine {self.model} is turned on"

appliance = Appliance()
washing_machine = WashingMachine(model="LG")

print(appliance.turn_on())
print(washing_machine.turn_on())

class PrivateData:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password

data = PrivateData("user1", "pass123")
print(data.get_username())
print(data.get_password())
data.set_password("newpass123")
print(data.get_password())


class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = Account("987654321", 5000)
account.deposit(1500)
account.withdraw(2000)
print(f'Balance: {account.get_balance()}')


class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def move(self):
        return f'{self.model} is driving'

class Bike(Vehicle):
    def __init__(self, model):
        self.model = model

    def move(self):
        return f'{self.model} is riding'

def operate_vehicle(vehicle):
    print(vehicle.move())

car = Car("Toyota")
bike = Bike("Yamaha")

operate_vehicle(car)
operate_vehicle(bike)