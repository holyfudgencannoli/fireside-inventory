from .read_by_id import read_by_id
from ...db import db_session

def delete_user(user_id):
    
    user = read_by_id(user_id)
    if user:
        db_session.delete(user)
        db_session.commit()
        return True
    return False