from sqlalchemy import Column, Integer, String,Boolean

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PinGenerateRequest():
    entity: str
    applicationId: str




