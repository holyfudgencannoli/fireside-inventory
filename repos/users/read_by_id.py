from models.user import User
from ...db import db_session

def read_by_id(user_id):
    return db_session.query(User).filter(User.id == user_id).first()