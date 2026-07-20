class GreetingMixin:
    def greet(self):
        print(f"Hello, I am {self.name}")
class Student(GreetingMixin):
    def __init__(self,name):
        self.name=name
class Teacher(GreetingMixin):
    def __init__(self,name):
        self.name=name
s=Student("Arun")
t=Teacher("Priya")
s.greet()
t.greet()    