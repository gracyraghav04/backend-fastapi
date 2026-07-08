from fastapi import FastAPI

app = FastAPI()

@app.get("/students/{id}")   #for resource identification:path parameter
def get_student(id: int):
    return {
        "student_id": id
    }
@app.get("/students")   #for fitering :query parameters
def get_students(age: int):
    return {
        "age": age
    }    

       

@app.get("/students/{id}")
def get_student(id: int, semester: int):  #both 
    return {
        "student_id": id,
        "semester": semester
    }