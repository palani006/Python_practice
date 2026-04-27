from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from passlib.context import CryptContext

app = FastAPI()

users = {}      
responses = []   

class Register(BaseModel):
    username: str
    password: str
    role: str  # "student" or "admin"

class Login(BaseModel):
    username: str
    password: str

class Response(BaseModel):
    username: str
    password: str
    training_rating: int = Field(ge=0,le=10)
    trainer_rating: int = Field(ge=0,le=10)
    content_quality: int = Field(ge=0,le=10)
    understanding_level: int = Field(ge=0,le=10)
    practical_knowledge: int = Field(ge=0,le=10)
    communication: int = Field(ge=0,le=10)
    doubts_cleared: str
    improvement_suggestions: str
    overall_feedback: str

def authenticate(username: str, password: str):
    user = users.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

@app.post("/register")
def register(user: Register):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")

    if user.role not in ["student", "admin"]:
        raise HTTPException(status_code=400, detail="Role must be student or admin")

    users[user.username] = {
        "password": user.password,
        "role": user.role
    }

    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: Login):
    db_user = users.get(user.username)

    if not db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "role": db_user["role"]
    }

@app.post("/student/submit")
def submit_response(data: Response):
    user = authenticate(data.username, data.password)

    if user["role"] != "student":
        raise HTTPException(status_code=403, detail="Only students allowed")

    response = {
        "student": data.username,
        "training_rating": data.training_rating,
        "behaviour": data.behaviour,
        "content_quality": data.content_quality,
        "understanding_level": data.understanding_level,
        "practical_knowledge": data.practical_knowledge,
        "communication": data.communication,
        "doubts_cleared": data.doubts_cleared,
        "improvement_suggestions": data.improvement_suggestions,
        "overall_feedback": data.overall_feedback
    }

    responses.append(response)

    return {"message": "Response submitted successfully"}

@app.get("/admin/responses")
def view_responses(username: str, password: str):
    user = authenticate(username, password)

    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin allowed")

    return {
        "total_responses": len(responses),
        "responses": responses
    }

@app.get("/")
def home():
    return users,responses