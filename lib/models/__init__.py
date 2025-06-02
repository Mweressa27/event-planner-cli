from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///event_planner.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

from .event import Event
from .guest import Guest
from .rsvp import RSVP