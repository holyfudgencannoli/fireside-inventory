from models import Authenticator
from db import db_session


def get_authenticator(authenticator_id: str):    
    authenticator = db_session.query(Authenticator).filter_by(id=authenticator_id).first()
    return authenticator