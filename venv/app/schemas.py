from pydantic import BaseModel

class FormDataIn(BaseModel):
    full_name: str
    phone: str
    address: str = None

class FormDataOut(FormDataIn):
    id: int
