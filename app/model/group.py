from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base

from typing import List
from pin import Pin

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=True, unique=True)
    description = Column(String(255),nullable=False)
    active = Column(Boolean, nullable=False,default=False)


