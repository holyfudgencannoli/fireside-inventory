from datetime import datetime, timedelta

from models import Event
from db import db_session
from uuid import uuid4
import hashlib

def create_event(
    user_id: int, 
    provider: str,
    expires_at: int = int((datetime.now() + timedelta(days=365)).timestamp()),
    provider_account_id: str = ""

):
    id = str(uuid4())

    event = Event(
        id=id,
        user_id=user_id,
        provider=provider,
        provider_account_id=provider_account_id,
        expires_at=expires_at
    )
    db_session.add(event)
    db_session.commit()
    db_session.refresh(event)
    return event