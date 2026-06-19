from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
std=[
    {"id":1,"name":"palani","age":23,"city":"kuppam"},
    {"id":2,"name":"rajesh","age":22,"city":"palamaneru"},
    {"id":3,"name":"nikhal","age":22,"city":"hyd"},
    {"id":4,"name":"lokesh","age":20,"city":"dkpalli"},
    {"id":5,"name":"veerendra","age":20,"city":"tankroad"},
]

@app.get("/stud/{stdt_id}")
def student_id(stdt_id: int):
    for student in std:
        if student["id"]==stdt_id:
            return student
    raise HTTPException(status_code=404, detail=f"Student with id {student_id} not found")


@app.get("/std/count")
def std_count():
    return {"total:": len(std)}

