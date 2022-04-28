from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Column

Base = declarative_base()

class WorkplaceType(Base):
    __tablename__ = 'workplaceTypes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Integer)

class Workplace(Base):
    __tablename__ = 'workplace'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer, ForeignKey('workplaceTypes.id'))
    sensors = relationship("Sensor", back_populates="workplace")
    worker = relationship("Worker", back_populates="workplace")

class Worker(Base):
    __tablename__ = 'worker'
    id = Column(Integer, primary_key=True, autoincrement=True)
    workplace = Column(Integer, ForeignKey('workplace.id'))


WORKPLACE_TYPES = [
    WorkplaceType(description="Single"),
    WorkplaceType(description="Dual"),
    WorkplaceType(desciption="Multi")
]

WORKPLACES = [
    Workplace(type=0),
    Workplace(type=0),
    Workplace(type=1),
    Workplace(type=2),
    Workplace(tyoe=2),
    Workplace(type=2),
    Workplace(type=1),
    Workplace(type=1)
]
