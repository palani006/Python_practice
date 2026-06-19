from jose import jwt,JWTError
from datetime import datetime,timedelta
SECRET_KEY="this-is-special-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIES_MINUTES=30

def create_token(username:str)->str:
    payload={
        "sub":username,
        "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIES_MINUTES)
    }
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token:str)->str:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    username=payload.get("sub")
    if not username:
        raise JWTError("token already taken")
    return username