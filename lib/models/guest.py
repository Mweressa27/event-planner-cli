from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    events = relationship("EventGuest", back_populates="guest")
