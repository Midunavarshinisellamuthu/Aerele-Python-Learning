class Employee:
    def __init__(self):
        self.name="Arun"
        self._salary=50000
        self.__age=40
e=Employee()
print(f"{e.name}->{e._salary}->{e.__age}")