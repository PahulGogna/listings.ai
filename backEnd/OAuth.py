from jose import JWTError, jwt
from datetime import datetime, timedelta
import Schemas
from fastapi import HTTPException,Depends,status
from fastapi.security import OAuth2PasswordBearer
import os

OAuth_schema = OAuth2PasswordBearer(tokenUrl="login")

# SECRET_KEY = config.get('SECRET_KEY')
SECRET_KEY = os.environ.get("SECRET_KEY") 
# ALGORITHM = config.get('ALGORITHM')
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        print(payload)
        id : str = payload.get("user_id")

        if payload is None:
            raise credentials_exception
        
        # exp_time = payload.exp
        # now = datetime.utcnow()

        # if exp_time > now:
        #     raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail="You have been logged out")
        
        token_data = Schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token:str = Depends(OAuth_schema)):

    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    return verify_access_token(token, credentials_exception)