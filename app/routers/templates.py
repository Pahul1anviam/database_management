from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app.database import get_db

router = APIRouter()

from fastapi import Depends
from sqlalchemy.orm import Session
from app import database, schemas, crud

@router.post("/templates/", response_model=schemas.TemplateOut)
def create_template(template: schemas.TemplateCreate, db: Session = Depends(database.get_db)):
    return crud.create_template(db, template)

# @router.get("/templates/", response_model=list[schemas.TemplateOut])
# def get_templates(db: Session = Depends(get_db)):
#     return crud.get_templates(db)
