import functools
import time
import random
#Higher-Order Function
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def greet():
    return "hello, world"
decrator_greet = uppercase_decorator(greet) #Applying decrator manually
print(decrator_greet())
print(uppercase_decorator(greet)())

#decrator pattern
@uppercase_decorator
def self_introduction():
    return 'hello, my name is Cindy'

print(self_introduction())


#decrator in class
def debug_decrator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with arguments {args} {kwargs}')
        return func(*args, **kwargs)
    return wrapper

class Calculator:
    @debug_decrator
    def add(self,a,b):
        return a+b

    @debug_decrator
    def print(self,x):
        return x

cal = Calculator()
print(cal.add(3,5))
print(cal.print(10))

# Logging Function Calls (Debugging Decorator)
#A logging decorator can help track function calls and their arguments.
def log_decorator(func):
    @functools.wraps(func)   # Preserves original function name and docstring
    def wrapper(*args, **kwargs):
        print(f'[DEBUG] Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'[DEBUG] {func.__name__} returned: {result}')
        return result
    return wrapper

@log_decorator
def add(a,b):
    return a+b
print(add(3,9))

#Authentication Decorator: Restricting Access to Authorized Users
#A user authentication decorator ensures that only authenticated users can access a function.
def auth_decrator(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_authenticated', False):
            raise PermissionError('User not authenticated!')
        return func(user, *args, **kwargs)
    return wrapper

@auth_decrator
def get_user_date(user:dict, data_id:int) -> str:
    return f"User {user['name']} accessed data {data_id}"

#Example users
authenticated_user = {"name": "Alice", "is_authenticated": True}
unauthenticated_user = {"name": "Bob", "is_authenticated": False}

print(get_user_date(authenticated_user, 101))
print(get_user_date(unauthenticated_user, 48))
# Ensures security and access control in web applications.
# Prevents unauthorized users from accessing sensitive data.

# Retry Mechanism for API Calls (Resilience)
# A retry decorator ensures that a function retries execution if it fails.
def retry_decrator(retries = 3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'Attempt {attempt+1} times failed: {e}')
                    time.sleep(delay)
            raise Exception('Max retries reached')
        return wrapper
    return decorator

@retry_decrator(retries=5, delay=2)
def unstable_api():
    if random.random()<0.7:
        raise ConnectionError('API is down!')
    return 'API response'

print(unstable_api())
