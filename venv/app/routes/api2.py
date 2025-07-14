from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import FormData
from app.schemas import FormDataOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/formData", response_model=list[FormDataOut])
def get_all_form_data(db: Session = Depends(get_db)):
    return db.query(FormData).all()
