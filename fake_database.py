from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []


class Student(BaseModel):
    name: str
    age: int


@app.post("/students")
def create_student(student: Student):

    students.append(student)

    return {
        "message": "Student Added Successfully"
    }


@app.get("/students")
def get_students():

    return students