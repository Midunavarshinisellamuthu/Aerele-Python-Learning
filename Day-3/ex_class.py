class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=Person("John",20)
obj2=Person("Emi",19)
print(f"{obj1.name} {obj1.age}")
print(f"{obj2.name} {obj2.age}")