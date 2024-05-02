from typing import Union, List

from pydantic import dataclasses
from mitypes import UserLite, DriveFile

@dataclasses.dataclass()
class posts:
    id: str
    createdAt: str
    updatedAt: str
    userId: str
    user: UserLite
    title: str
    description: Union[str, None]
    fileIds: List[str]
    files: DriveFile
    tags: List[str]
    isSensitive: bool
    likedCount: int
    isLikes: bool