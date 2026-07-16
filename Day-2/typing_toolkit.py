from typing import Optional
def greet(name:Optional[str]):
    if name is None:
        print("Guest")
    else:
        print(name)
greet(None)

