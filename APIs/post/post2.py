from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

student=[]
s_id=1

class students(BaseModel):
    name: str
    age: int
    marks: int
    post: str

@app.post("/sttd",status_code=201)
def studde(student :students):
    global s_id
    new_std={
        "name":studde.name,
        "age":studde.int,
        "marks":studde.marks,
        "post":studde.post
    }

    student.append(new_std)
    s_id+=1
    return new_std