from .read_by_id import read_by_id
from ...db import db_session

def update_user(user_id, name=None, email=None, password_hash=None):

    user = read_by_id(user_id)
    if not user:
        return None

    if name is not None:
        user.name = name
    if email is not None:
        user.email = email
    if password_hash is not None:
        user.password_hash = password_hash

    db_session.commit()
    db_session.refresh(user)
    return user.to_dict()