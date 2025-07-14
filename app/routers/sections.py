from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload 
from app import schemas, crud, database
from app.database import get_db
from typing import List
from app import models
from fastapi import Query
from typing import Optional


router = APIRouter()

@router.post("/templates/{template_id}/sections/", response_model=schemas.SectionOut)
def create_section(template_id: int, section: schemas.SectionCreate, db: Session = Depends(get_db)):
    return crud.create_section(db, template_id, section)

# @router.get("/templates/{template_id}/sections/", response_model=list[schemas.SectionOut])
# def get_sections(template_id: int, db: Session = Depends(get_db)):
#     return crud.get_sections_by_template(db, template_id)

@router.get("/templates_with_sections/", response_model=List[schemas.TemplateWithSections])
def get_templates_with_sections(
    user_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Template).options(joinedload(models.Template.sections))

    if user_id is not None:
        query = query.filter(models.Template.user_id == user_id)

    return query.all()



@router.get("/get_sections_combined/")
def get_combined_sections(user_id: int = Query(...), template_id: int = Query(...), db: Session = Depends(get_db)):
    # Validate template belongs to user
    template = db.query(models.Template).filter_by(id=template_id, user_id=user_id).first()
    if not template:
        return {"error": "Invalid user_id or template_id"}

    sections = db.query(models.Section).filter_by(template_id=template_id).all()

    combined = ""
    for section in sections:
        combined += f"{section.section_name}: {section.section_description}\n\n"

    return {"sections_combined": combined.strip()}

