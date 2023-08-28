import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()


class intializeDB():
    def createDBSession():
        dbStr = ""+os.environ.get("DB_DAILECT")+"://"+os.environ.get("DB_USER")+":"+os.environ.get("DB_PASS")+"@"+os.environ.get("DB_HOST")+":"+os.environ.get("DB_PORT")+"/"+os.environ.get("DB_NAME")+""
        engine = create_engine(dbStr, echo=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
    
        Base = declarative_base()

        return session

