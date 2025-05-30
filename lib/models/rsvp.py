from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class RSVP(Base):
    __tablename__ = 'rsvps'
    id = Column(Integer, primary_key=True)
    status = Column(String)

    event_id = Column(Integer, ForeignKey('events.id'))
    guest_id = Column(Integer, ForeignKey('guests.id'))

    event = relationship("Event", back_populates="rsvps")
    guest = relationship("Guest", back_populates="rsvps")

    def __repr__(self):
        return f"<RSVP: {self.guest.name} → {self.event.title} = {self.status}>"
