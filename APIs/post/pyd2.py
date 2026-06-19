from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

sta = []
s_id = 1



class Mode(BaseModel):
    name: str
    age: int
    city: str

@app.post("/sta", status_code=201)
def stud(stdd: Mode):
    global s_id
    new_stdd = {
        "id": s_id,
        "name": stdd.name,
        "age": stdd.age,
        "city": stdd.city
    }
    sta.append(new_stdd)
    s_id += 1
    return new_stdd
