from fastapi import FastAPI
from app.database import Base, engine
from app.routers import student


app = FastAPI(title=" Student API with SQLite")

#crate all tables
Base.metadata.create_all(bind=engine)

# attach routers

app.include_router(student.router)