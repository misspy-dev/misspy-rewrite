from typing import Union

from pydantic import dataclasses
from mitypes.user import UserLite
from mitypes.drive import DriveFile

@dataclasses.dataclass()
class GalleryPost:
    id: str
    createdAt: str
    updatedAt: str
    userId: str
    user: UserLite
    title: str
    description: Union[str, None]
    fileIds: list[str]
    files: list[DriveFile]
    tags: list[str]
    isSensitive: bool
    likedCount: int
    isLikes: bool

@dataclasses.dataclass()
class Like:
    id: str
    post: GalleryPost