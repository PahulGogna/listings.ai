import models
from sqlalchemy.orm import Session
from database import engine, sessionLocal, get_db
from fastapi.responses import HTMLResponse
from fastapi import Depends,FastAPI
import users
import listings
import OAuth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(listings.router)

@app.get("/")
def ads(db: Session = Depends(get_db),current_user : int = Depends(OAuth.get_current_user)):
    try:
        return db.query(models.Users).all()
    except Exception as e:
        print(e)


@app.get("/form", response_class=HTMLResponse,)
async def get_form(current_user : int = Depends(OAuth.get_current_user)):
    with open("../frontEnd/form.html","r") as f:
        file = f.read()
    return file