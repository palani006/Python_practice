from fastapi import FastAPI,HTTPException
from  pydantic import BaseModel,Field

app = FastAPI()

class rajesh(BaseModel):
    name: str = Field(min_length=4,max_length=70)
    age: int = Field(gt= 19 , lt= 50)
    email: str = Field(min_length=4)
    phn_no: int 
    city: str = Field(default= "unknown",max_length=100)

k=[]

@app.post("/ra",status_code=201)
def common(student:rajesh):
    new= {
        "id":1,
        "name":student.name,
        "age":student.age,
        "email":student.email,
        "phn_no":student.phn_no,
        "city":student.city
    }
    k.append(new)
    return new


@app.get("/rajju")
def read():
    return k