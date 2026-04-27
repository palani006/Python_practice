from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from passlib.context import CryptContext

app = FastAPI()

user ={}
responsee = []

class registration(BaseModel):
    username:str
    password:str
    role:str

class login(BaseModel):
    username:str
    password:str

class response(BaseModel):
    username:str
    password:str
    Explanation:int=Field(ge=1,le=5)
    Explanation_about_examples:int=Field(ge=1,le=5)
    Behaviour:int=Field(ge=1,le=5)
    Their_knowledge_on_subject:int=Field(ge=1,le=5)
    Positive_about_prgm:str
    Improving:str
    Today_session:str
    Suggestion:str

def authentication(username:str,password:str):
    users=user.get(username)
    if users is None or users["password"]!=password:
        return None
    return users

@app.post("/Register")
def regester(userr:registration):
    user[userr.username]={
        "password":userr.password,
        "role":userr.role
    }
    return {"msg":"user registered sucessfully"}

@app.post("/Login")
def login(usser:login):
    s_user=authentication(usser.username,usser.password)

    if not s_user or s_user["password"]!=usser.password:
        raise HTTPException(status_code=400,detail=f"Invalid details")
    
    return {
     "msg":"login successfully",
     "role":s_user["role"]
    }

@app.post("/student/submit")
def submit(details:response):
    uuser=authentication(details.username,details.password)

    if not uuser:
        raise HTTPException(status_code=401,detail="invalid user")
    if uuser["role"]!="student":
        raise HTTPException(status_code=403,detail=f"only students allowed")
    new_response={
        "username":details.username,
        "password":details.password,
        "Explanation":details.Explanation,
        "Explanation_about_examples":details.Explanation_about_examples,
        "Behaviour":details.Behaviour,
        "Their_knowledge_on_subject":details.Their_knowledge_on_subject,
        "Positive_about_prgm":details.Positive_about_prgm,
        "Improving":details.Improving,
        "Today_session":details.Today_session,
        "Suggestion":details.Suggestion,
    }
    responsee.append(new_response)
    return new_response

@app.get("/")
def show():
    return {
        "msg":"hi"
    }

@app.get("/s")
def hi():
    return user

@app.get("/responses")
def get_responses():
    return responsee
