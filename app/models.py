from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship



class Template(Base):
    __tablename__ = "templates"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    template_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    sections = relationship("Section", back_populates="template", cascade="all, delete-orphan")



class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("templates.id", ondelete="CASCADE"))
    section_name = Column(String, nullable=False)
    section_description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    template = relationship("Template", back_populates="sections")
