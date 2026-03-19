from .get import get_event
from .list import list_events
from .delete import delete_event
from .create import create_event

create = create_event
get = get_event
list = list_events
delete = delete_event

__all__ = [
    "create",
    "get",  
    "list",
    "delete"
]