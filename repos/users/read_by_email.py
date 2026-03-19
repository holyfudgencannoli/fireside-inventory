from models.user import User
from ...db import db_session

def read_by_email(email):
    return db_session.query(User).filter(User.email == email).first()