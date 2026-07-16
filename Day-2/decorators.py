def sample(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@sample
def greet():
    print("Hello")
greet()     