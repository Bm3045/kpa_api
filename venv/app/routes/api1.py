from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import FormData
from app.schemas import FormDataIn, FormDataOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/formData", response_model=FormDataOut)
def create_form_data(data: FormDataIn, db: Session = Depends(get_db)):
    new_data = FormData(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data
