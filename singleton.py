'''When you need only one instance (e.g., database connections, configuration managers)'''
'''Ensures that a class has only one instance and provides a global point of access to it.'''
class Singleton:
    _instance = None #class-level attribute

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

'''Connect PostgreSQL with psycogp2'''
import psycopg2
class DataConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = psycopg2.connect(
                datebase = '',
                user='',
                password='',
                host='',
                port=''
            )
            print('Database connection established.')
        return cls._connection
conn1 = DataConnection.get_connection()
conn2 = DataConnection.get_connection()
print(conn1 is conn2)

'''Example of maintaining a single copy of an application stay'''
class Applicationstate:
    instance = None

    def __init__(self):
        self.is_logged_in = False

    @staticmethod
    def get_app_state():
        if not Applicationstate.instance:
            Applicationstate.instance = Applicationstate()
        return Applicationstate.instance

app_state1 = Applicationstate.get_app_state()
print(app_state1.is_logged_in) #False

app_state2 = Applicationstate.get_app_state()
print(app_state2.is_logged_in)#False
app_state1.is_logged_in = True
print(app_state2.is_logged_in)#True
