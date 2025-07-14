from sqlalchemy import Column, Integer, String
# from kpa_api_assignment.db import Base
from db import Base


class FormData(Base):
    __tablename__ = "form_data"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=True)
