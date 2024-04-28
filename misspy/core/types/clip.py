from typing import Union

from pydantic import dataclasses
from mitypes import UserLite

@dataclasses.dataclass()
class clips:
    id: str
    createdAt: str
    lastClippedAt: Union[str, None]
    userId: str
    user: UserLite
    name: str
    description: Union[str, None]
    isPublic: bool
    favoritedCount: int
    isFavorited: bool