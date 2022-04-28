from sqlalchemy.orm import declarative_base
from sqlalchemy.types import String, Integer
from sqlalchemy import Column

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


SENSORS = [
    Sensor(name="BLADL_00_001"),
    Sensor(name="BLADL_00_002"),
    Sensor(name="BLADL_00_003"),
    Sensor(name="BLADL_00_004"),
    Sensor(name="BLADL_00_005"),
    Sensor(name="BLADL_00_006"),
    Sensor(name="BLADL_00_007"),
    Sensor(name="BLADL_00_008"),
    Sensor(name="BLADL_00_009"),
    Sensor(name="BLADL_00_010"),
    Sensor(name="BLADL_00_011"),
    Sensor(name="BLADL_00_012"),
    Sensor(name="BLADL_00_013"),
    Sensor(name="BLADL_00_014"),
    Sensor(name="BLADL_00_015"),
    Sensor(name="BLADL_00_016"),
    Sensor(name="BLADL_00_017"),
    Sensor(name="BLADL_00_018"),
    Sensor(name="BLADL_00_019"),
    Sensor(name="BLADL_00_020"),
    Sensor(name="BLADL_00_021"),
    Sensor(name="BLADL_00_022"),
    Sensor(name="BLADL_00_023"),
    Sensor(name="BLADL_00_024"),
    Sensor(name="BLADL_00_025"),
    Sensor(name="BLADL_00_026"),
    Sensor(name="BLADL_00_027"),
    Sensor(name="BLADL_00_028"),
    Sensor(name="BLADL_00_029"),
    Sensor(name="BLADL_00_030"),
    Sensor(name="BLADL_00_031"),
    Sensor(name="BLADL_00_032"),
    Sensor(name="BLADL_00_033"),
    Sensor(name="BLADL_00_034"),
    Sensor(name="BLADL_00_035"),
    Sensor(name="BLADL_00_036")
]
