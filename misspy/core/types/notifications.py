from pydantic import dataclasses
from mitypes.user import UserLite

from .note import Note

@dataclasses.dataclass()
class notifications:
    id: str
    createdAt: str
    type: str
    user: UserLite
    userId: str
    note: Note