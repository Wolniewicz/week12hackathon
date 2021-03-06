import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Model
 
engine = create_engine('sqlite:///models.db', echo=True)


# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
#Create several models
m1 = Model("chair","/img/chair.jpg")

# Add the record to the session object
session.add_all([m1])
# commit the record the database
session.commit()
 
