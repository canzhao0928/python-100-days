class User:
    def __init__(self, name) :
        self.name = name
        self.is_logined_in =False

def is_auth_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logined_in == True:
            function(args[0])
    return wrapper


@ is_auth_decorator
def welcome(user):
    print(f"Welcone {user.name}")

user=User("Can")
user.is_logined_in=True
welcome(user)
        