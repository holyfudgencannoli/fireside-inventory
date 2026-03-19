from db import db_session
from models.user import User

def create_user(name, email, password_hash):
    new_user = User(
        name=name, 
        email=email, 
        password_hash=password_hash
    )

    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user.to_dict()