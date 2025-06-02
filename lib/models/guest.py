from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Guest(Base):
    __tablename__ = 'guests'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    rsvps = relationship("RSVP", back_populates="guest", cascade="all, delete")

    def __repr__(self):
        return f"<Guest {self.name} ({self.email})>"
