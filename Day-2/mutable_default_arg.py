def add(num,lst=None):
    if lst is None:
        lst=[]
    lst.append(num)
    return lst
print(add(1))
print(add(2))