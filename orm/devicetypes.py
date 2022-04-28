from sqlalchemy.orm import declarative_base
from sqlalchemy.types import String, Integer
from sqlalchemy import Column

Base = declarative_base()

class DeviceType(Base):
    __tablename__ = "deviceType"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    PC = 1
    Monitor = 2
    Utility = 3
    Printer = 4