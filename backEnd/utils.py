from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import get_db
from fastapi.params import Depends

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")


def hash(password):
    return pwd_context.hash(password)

def verify(input_password, hashed_password):
    return pwd_context.verify(input_password,hashed_password)

def save_listing(listing: dict, db: Session = Depends(get_db)):
    db.add(**listing)
    db.commit()
    db.refresh(listing)
    return listing