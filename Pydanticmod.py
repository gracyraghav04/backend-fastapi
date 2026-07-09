from fastapi import FastAPI
from pydantic import BaseModel


class Student(BaseModel):  #the class is a pydantic model;It is a blueprint thar describes what type of data the client is suppose to recieve.
    name: str              #FastAPI plus pydantic converts the json to a python object
    age: int


from fastapi import FastAPI


app = FastAPI()



@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student Created Successfully",
        "student": student
    }    