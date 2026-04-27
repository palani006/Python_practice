from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()

p_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashpass(passward:str)->str:
    return p_context.hash(passward)

def verifypass(plani_password:str, hash_password:str)->bool:
    return p_context.verify(plani_password,hash_password)

db = []

class registration(BaseModel):
    u_name:str
    p_word:str

class login(BaseModel):
    u_name:str
    p_word:str

@app.get("/read")
def read():
    return {
        "msg":"wellcom"
    }

@app.post("/user")
def reg(user: registration):
    for i in db:
        if i["u_name"] == user.u_name:
            raise HTTPException(status_code=401,detail="username is already taken")
    
    hashed = hashpass(user.p_word) 

    u_new= {
        "id":len(db)+1,
        "u_name":user.u_name,
        "p_word":hashed,
    }

    db.append(u_new)
    return {"account was created sucessfully" :{user.u_name} }


@app.post("/login")
def login(user : login):
    found_user=None
    for i in db:
        if i["u_name"]==user.u_name:
            found_user=i
            break
    if not found_user:
        raise HTTPException(status_code=401,detail=f"user not forund")
    if not verifypass(user.p_word , found_user["p_word"]):
        raise HTTPException(status_code=401,detail="invalid details")
    
    return {"msg": "login successfully","user":user.u_name}

@app.get("/update")
def detailes():
    return db