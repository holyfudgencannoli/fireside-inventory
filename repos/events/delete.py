from models import Event
from db import db_session

def delete_event(event_id: str):

    event = db_session.query(Event).filter_by(id=event_id).first()
    if event:
        db_session.delete(event)
        db_session.commit()
        return True
    return False