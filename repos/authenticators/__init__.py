from .get import get_authenticator
from .list import list_authenticators
from .delete import delete_authenticator
from .create import create_authenticator

create = create_authenticator
get = get_authenticator
list = list_authenticators
delete = delete_authenticator

__all__ = [
    "create",
    "get",  
    "list",
    "delete"
]