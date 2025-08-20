from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    # name:str = 'sourav' default values
    name:str
    age:Optional[int] = None #need to set a default value if we use optional
    # email:EmailStr
    cgpa:float = Field(gt=0,lt=10,description="A decimal value representing the cgpa of the student")


new_student = {'name':'sourav','age':'22','cgpa':7.8} # it can also do type conversion by its own when required

student = Student(**new_student)

student_dict = dict(student)

print(student_dict)