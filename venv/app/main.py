from fastapi import FastAPI
from app.routes import api1, api2
from db import Base, engine
from django.db import router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api1.router)
app.include_router(api2.router)
