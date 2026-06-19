from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = [
    {"id": 1, "name": "Ravi",  "age": 20, "address": "Kuppam"},
    {"id": 2, "name": "Priya", "age": 21, "address": "Chennai"},
]

s_id = 3

class Student(BaseModel):
    name: str
    age: int
    address: str

@app.get("/stu")
def read():
    return students

@app.post("/sttd",status_code=201)
def create_new_student(student :Student):
    global s_id
    new_std={
        "id": s_id,
        "name":student.name,
        "age":student.age,
        "address":student.address
    }

    students.append(new_std)
    s_id+=1
    return new_std

@app.put("/std")
def update_student(student_id: int, student_data: Student):
    for i, sud in enumerate(students):
        if sud["id"] == student_id:
            students[i] = {
                "id": student_id,
                "name": student_data.name,
                "age": student_data.age,
                "address": student_data.address
            }
            return students[i]
        
    raise HTTPException(status_code=404, detail=f"Student with id {student_id} not found")

@app.delete("/student")
def delete_student(student_id: int):
    for i,s1 in enumerate(students):
        if s1["id"]==student_id:
            delete=students.pop(i)
            return{"msg": f"name:'{delete['name']}'deleted sucessfully "}
    raise HTTPException(status_code=404,details=f"Student with this id {student_id} not found")