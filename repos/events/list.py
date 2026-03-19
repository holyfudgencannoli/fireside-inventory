from models import event
from db import db_session


def list_events(user_id: int):
    events = db_session.query(event).filter_by(user_id=user_id).all()
    return events