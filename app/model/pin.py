from typing import List
from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pin(Base):
    __tablename__ = "pins"
    id = Column(Integer, primary_key=True)
    pin = Column(String(80), nullable=True, unique=True)
    group_id = Column(Integer, nullable=True)
    entity = Column(String(80),nullable=False)
    active = Column(Boolean, nullable=False,default=False)



