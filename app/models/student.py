from sqlalchemy import Column, Integer, String
from app.database import Base

class Student(Base):
    __tablename__ = "Students"
 

    id = Column(Integer, primary_key = True, index=True)
    age = Column(Integer, index= True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    CNIC = Column(String, unique=True, index=True)



  

