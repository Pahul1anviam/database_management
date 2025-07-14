from sqlalchemy.orm import Session
from app import models, schemas
import random
import html

def create_template(db: Session, template: schemas.TemplateCreate):
    safe_name = html.escape(template.template_name)  # HTML-safe conversion

    db_template = models.Template(
        template_name=safe_name,
        user_id=template.user_id
    )
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

# def get_templates(db: Session):
#     return db.query(models.Template).all()

def create_section(db: Session, template_id: int, section: schemas.SectionCreate):
    safe_name = html.escape(section.section_name)
    safe_description = html.escape(section.section_description)

    db_section = models.Section(
        template_id=template_id,
        section_name=safe_name,
        section_description=safe_description
    )
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section

def get_sections_by_template(db: Session, template_id: int):
    return db.query(models.Section).filter(models.Section.template_id == template_id).all()
