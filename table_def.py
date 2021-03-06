# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///models.db', echo=True)
Base = declarative_base()
 
########################################################################
class Model(Base):
    """"""
    __tablename__ = "Models"
 
    id = Column(Integer, primary_key=True)
    name = Column(String) 
    img_path = Column(String) 
 
    #----------------------------------------------------------------------
    def __init__(self, name, img_path):
        """"""
        self.name = name
        self.img_path = img_path
 
########################################################################
 
# create tables
Base.metadata.create_all(engine)
