from enum import Enum
class Season(Enum):
    Spring=1
    Autum=2
    Summer=3
    Winter=4
print(Season.Spring)
print(Season.Spring.value)
