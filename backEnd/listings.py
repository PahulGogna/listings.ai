from fastapi import HTTPException,status,APIRouter,Depends,File, UploadFile, Form
from fastapi.responses import HTMLResponse
import Schemas
import OAuth
from sqlalchemy.orm import Session
from database import get_db
import models
from typing import List 
import AI

router = APIRouter()

@router.post("/listings")
async def create_listing(title: str = Form(...), description: str = Form(...), images: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    
    global data

    data = (title, description, images)
    return {"done"}



    