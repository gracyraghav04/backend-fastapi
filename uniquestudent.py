from fastapi import FastAPI
from pydantic import Basemodel
from fastapi import HTTPException
students=[]
app=FastAPI()
class Student(Basemodel):
    name:str
    age:int
@app.post("/students")
def create_student(student : Student):
    students.append(student)
    return{
        "message":"Student Added Successfully"
    }
@app.get("/students"):
def get_students():
    return students    

@app.get("/students/{id}")
def get_student(id:int):
    if id>=len(students):
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    return students[id]