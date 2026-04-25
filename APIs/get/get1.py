from fastapi import FastAPI,HTTPException
std=[
    {"id":1,"name":"palani","age":23,"city":"kuppam"},
    {"id":2,"name":"rajesh","age":22,"city":"palamaneru"},
    {"id":3,"name":"nikhal","age":22,"city":"hyd"},
    {"id":4,"name":"lokesh","age":20,"city":"dkpalli"},
    {"id":5,"name":"veerendra","age":20,"city":"tankroad"},
]

app=FastAPI()
@app.get("/")
def clas():
    return{
        "msg":"hi,hello"
    }
@app.get("/std/good")
def loos():
    return{"total":len(std)}

@app.get("/hi/{student_id}")
def stuuu(student_id: int):
    for studen in std:
        if studen[id]==student_id:
            return student_id
    raise HTTPException(statsu_code=404 ,detail=f"student is{student_id}not found")
