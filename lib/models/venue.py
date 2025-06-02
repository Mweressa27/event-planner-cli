from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer)

    events = relationship("Event", back_populates="venue")
