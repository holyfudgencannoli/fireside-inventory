from models import Authenticator
from db import db_session

def delete_authenticator(authenticator_id: str):

    authenticator = db_session.query(Authenticator).filter_by(id=authenticator_id).first()
    if authenticator:
        db_session.delete(authenticator)
        db_session.commit()
        return True
    return False