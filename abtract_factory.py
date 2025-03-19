from abc import ABC, abstractmethod
import psycopg2
import sqlite3

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass

class LightButton(Button):
    def render(self):
        return "Rendering Light Button"

class LightCheckBox(CheckBox):
    def render(self):
        return "Rendering Light Checkbox"

class DarkButton(Button):
    def render(self):
        return "Rendering Dark Button"

class DarkCheckbox(CheckBox):
    def render(self):
        return "Rendering Dark Checkbox"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass

class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> CheckBox:
        return LightCheckBox()

class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> CheckBox:
        return DarkButton()

#Client code
def render_ui(factory: UIFactory):
    button = factory.create_button()
    check_box = factory.create_checkbox()

    return  button.render(),check_box.render()

#example usage
light_factory = LightThemeFactory()
dark_factory = DarkThemeFactory()

print(render_ui(light_factory))
print(render_ui(dark_factory))

# Example for database connection
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class SQLiteConnection(DatabaseConnection):
    def connect(self):
        return sqlite3.connect('example.db')

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return psycopg2.connect(database="test", user="postgres", password="password", host="localhost", port="5432")

class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass

class MySQLFactory(DatabaseFactory):
    def create_connection(self)  -> DatabaseConnection:
        return SQLiteConnection()

class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

#Client code
def db_connection(facotry: DatabaseFactory):
    db_factory = facotry.create_connection()
    conn = db_factory.connect()
    print(f'Connected to {conn}')

#Example usage
mysql_factory = MySQLFactory()
postgresql_factory = PostgreSQLFactory()

print('Using MySQL:')
db_connection(mysql_factory)

print('Using PostgreSQL:')
db_connection(postgresql_factory)
