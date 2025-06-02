from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class EventGuest(Base):
    __tablename__ = 'event_guests'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    guest_id = Column(Integer, ForeignKey('guests.id'))

    event = relationship("Event", back_populates="guests")
    guest = relationship("Guest", back_populates="events")
