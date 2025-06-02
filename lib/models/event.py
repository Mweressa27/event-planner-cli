from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(Date)
    venue_id = Column(Integer, ForeignKey('venues.id'))

    venue = relationship("Venue", back_populates="events")
    guests = relationship("EventGuest", back_populates="event")
