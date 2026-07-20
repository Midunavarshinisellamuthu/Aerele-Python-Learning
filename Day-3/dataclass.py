from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age:int
    mark:int
s=Student("Abi",20,576)
print(s)