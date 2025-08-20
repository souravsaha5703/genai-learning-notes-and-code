from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person:Person = {'name':"sourav",'age':22}
print(new_person)