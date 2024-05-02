from typing import Union

from pydantic import dataclasses

from .users import UserDetailedNotMe

@dataclasses.dataclass()
class mute:
    id: str
    createdAt: str
    expiresAt: Union[str, None]
    muteeId: str
    mutee: UserDetailedNotMe