class Person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,salary):
        if salary<0:
            raise "Error"
        else:
            self._salary=salary
p=Person("Mano",27000)
p.salary=28000
print(p.salary)