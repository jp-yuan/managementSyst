from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "mysql+pymysql://root:jianpeng0122@localhost:3306/schoolapplication"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit= False, autoflush = False, bind = engine)

Base = declarative_base()

