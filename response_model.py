from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


students = []




class Student(BaseModel):
    name: str
    age: int
    password: str



class StudentResponse(BaseModel):
    name: str
    age: int


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    
)

def create_student(student: Student):

    students.append(student)

    return student

