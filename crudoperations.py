from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
students=[]
app=FastAPI()
class Student(BaseModel):
    name:str
    age:int
@app.post("/students")
def create_student(student : Student):
    students.append(student)
    return{
        "message":"Student Added Successfully"
    }
@app.get("/students")
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
@app.put("/students/{id}")
def update_student(id:int,student:Student):
    if id>=len(students):
        raise HTTPException(
            status_code=404,
            detail="student not found"
        ) 
    students[id]=student
    return{
        "message":"Student Updated Successfully",
        "student" : student
    }
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id >= len(students):

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message":"Student Deleted Successfully",
        "student": deleted_student
    }