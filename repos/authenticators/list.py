from models import Authenticator
from db import db_session


def list_authenticators(user_id: int):

    authenticators = db_session.query(Authenticator).filter_by(user_id=user_id).all()
    return authenticators