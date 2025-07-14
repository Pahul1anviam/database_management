from fastapi import FastAPI
from app.database import Base, engine
from app.routers import templates, sections

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Template Manager API")

app.include_router(templates.router)
app.include_router(sections.router)
