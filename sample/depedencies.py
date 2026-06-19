from fastapi import HTTPException,Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from jose import JWTError
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from utils.jwt import verify_token

baerer_schema=HTTPBearer()

def get_user(
        credentials:HTTPAuthorizationCredentials=Depends(baerer_schema),
        db:Session=Depends(get_db)
):
    token=credentials.credentials
    try:
        username=verify_token(token)
    except:
        raise HTTPException(status_code=401,detail="token is invalid or expired !")
    user=db.query(User).filter(User.username==username).first()
    if not user:
        raise HTTPException(status_code=401,detail="user not found")
    
    return user