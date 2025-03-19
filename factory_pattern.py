from abc import ABC, abstractmethod
import psycopg2
import sqlite3

'''Example of shapes factory'''
def Shape(ABC):
    '''Shape is an abstract base class (or interface) for all shape types.'''
    @abstractmethod
    def draw(self) ->str:
        '''Subclass must be implemented'''
        pass


class Circle:
    def draw(self) -> str:
        return 'Drawing a circle'

class Rectangle:
    def draw(self) -> str:
        return 'Drawing a rectangle'

class Square:
    def draw(self) -> str:
        return 'Drawing a square'

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type:str) -> Shape:
        '''Createing instances of different shape types based on input.'''
        if shape_type == 'Circle':
            return Circle()
        elif shape_type == 'Rectangle':
            return Rectangle()
        elif shape_type == 'Square':
            return Square()
        else:
            raise ValueError('Unknow shape type')

#usage
circle1 = ShapeFactory.get_shape('Circle')
print(circle1.draw())
# Advantage: If we add a new shape (Triangle), we modify only the ShapeFactory, not the client code.

#Factory Pattern for Database Connection Example
class PostgreSQLConnection:
    def connect(self):
        return psycopg2.connect(
            database='',
            user='',
            password='',
            host='',
            port=''
        )

class SQLiteConnection:
    def connect(self):
        return sqlite3.connect('example.db')

class DatabaseFactory:
    @staticmethod
    def get_connect(database_type):
        if database_type == 'PostgreSQL':
            return PostgreSQLConnection()
        elif database_type == 'SQLite':
            return SQLiteConnection()
        else:
            raise ValueError('Unknow database type')
#usage
db = DatabaseFactory.get_connect('PostgreSQL')
connection = db.connect()
print('Connected to PostgreSQL')

db2 = DatabaseFactory.get_connect('SQLite')
connection2 = db2.connect()
print('Connected to SQLite')

#Example of different notifications in an app
class Notification(ABC):
    @abstractmethod
    def send(self, message:str):
        pass

class EmailNotification(Notification):
    def send(self, message:str) -> str:
        return f'Sending email with message: {message}'

class SMSNotification(Notification):
    def send(self, message:str) -> str:
        return f'Sending SMS with message: {message}'

class NotificationFactory:
    @staticmethod
    def get_notification(notification_type:str) -> Notification:
        if notification_type == 'Email':
            return EmailNotification()
        elif notification_type == 'SMS':
            return SMSNotification()
        else:
            raise ValueError('Unknow notification type')

#useage of the factory
email = NotificationFactory.get_notification('Email')
print(email.send("It's from email"))

sms = NotificationFactory.get_notification('SMS')
print(sms.send("Hello from SMS"))

# Example of burger
class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
    def create_cheese_burger(self) -> Burger:
        ingredients = ['bun','cheese','beef-patty']
        return Burger(ingredients)

    def create_deluxe_cheese_burger(self) -> Burger:
        ingredients = ['bun','tomatoe', 'lettuce','cheese','beef-patty']
        return Burger(ingredients)

    def create_vegan_burger(self) -> Burger:
        ingredients = ['bun', 'special-sauce', 'veggie-patty']
        return Burger(ingredients)

burger = BurgerFactory()
burger.create_cheese_burger().print()
burger.create_deluxe_cheese_burger().print()
