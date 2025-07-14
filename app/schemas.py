from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from typing import List



class TemplateCreate(BaseModel):
    template_name: str
    user_id: int  


class TemplateOut(BaseModel):
    id: int
    template_name: str
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class SectionCreate(BaseModel):
    section_name: str
    section_description: Optional[str] = None

class SectionOut(BaseModel):
    id: int
    section_name: str
    section_description: Optional[str]
    template_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class TemplateWithSections(BaseModel):
    id: int
    template_name: str
    user_id: int
    created_at: datetime
    sections: List[SectionOut]

    class Config:
        orm_mode = True