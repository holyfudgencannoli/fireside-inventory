from models import Event
from db import db_session


def get_event(event_id: str):    
    event = db_session.query(Event).filter_by(id=event_id).first()
    return event