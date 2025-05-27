# car_cli/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class Car(Base):
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    color = Column(String)
    
    def __repr__(self):
        return f"<Car(make='{self.make}', model='{self.model}', year={self.year})>"