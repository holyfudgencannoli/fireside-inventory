from .create import create_user
from .read_by_email import read_by_email
from .read_by_id import read_by_id  
from .update import update_user
from .delete import delete_user

create = create_user
update = update_user
delete = delete_user

__all__ = [
    "create",
    "read_by_email",
    "read_by_id",
    "update",
    "delete"
]