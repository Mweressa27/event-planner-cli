from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from . import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    location = Column(String)
    date = Column(Date)
    rsvps = relationship("RSVP", back_populates="event", cascade="all, delete")
    
    def __repr__(self):
        return f"<Event {self.title} on {self.date}>"
