from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Belinda",
        "age": 18,
        "year": "Y3D"
    },
    2: {
        "name": "Jonathan",
        "age": 19,
        "year": "Y3D"
    },
    3: {
        "name": "Sofia",
        "age": 17,
        "year": "Y3C"
    },
    4: {
        "name": "Michael",
        "age": 18,
        "year": "Y3B"
    },
    5: {
        "name": "Emily",
        "age": 20,
        "year": "Y3D"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(description="The ID of the student you want to view", gt=0, lt=30)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int): #None to no longer make it required
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student Not Found"}

    if student.name is not None:
        students[student_id].name = student.name

    if student.age is not None:
        students[student_id].age = student.age

    if student.year is not None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student Not Found"}

    del students[student_id]
    return {"Message": f"Student {student_id} deleted successfully"}