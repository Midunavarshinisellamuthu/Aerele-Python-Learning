#positional arguments
def greet(name,age):
    print(f"Name: {name}, Age: {age}")
greet("Abi",19)

#keyword arguements
def student(name,mark):
    print(f"{name}->{mark}")
student(mark=520,name="Anu")

#default arguements
def info(name,city="Chennai"):
    print(f"{name} lives in {city}")
info("Anu")
info("Abi","Erode")

#*args
def add(*num):
    print(sum(num))
add(10,20)
add(10,20,30)

#**kwargs
def student(**details):
    print(details)
student(name="Ram",age=22,city="Erode")