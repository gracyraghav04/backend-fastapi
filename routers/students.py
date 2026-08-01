from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

students = []

@router.get("/")
def get_students():
    return students


@router.post("/")
def create_student():
    student = {
        "id": 1,
        "name": "Gracy",
        "age": 20
    }

    students.append(student)

    return {
        "message": "Student created successfully",
        "student": student
    }