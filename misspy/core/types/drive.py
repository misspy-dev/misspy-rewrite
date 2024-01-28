import dataclasses
from typing import Union

from .user import User

@dataclasses.dataclass
class DriveFolder:
    id: str
    createdAt: str
    name: str
    foldersCount: int
    filesCount: int
    parentId: str
    parent: dict

@dataclasses.dataclass
class df_property:
    width: int
    height: int
    orientation: int
    avgColor: str

@dataclasses.dataclass
class DriveFile:
    id: str
    createdAt: str
    name: str
    type: str
    md5: str
    size: int
    isSensitive: bool
    blurhash: Union[str, None]
    properties: df_property
    url: Union[str, None]
    thumbnailUrl: Union[str, None]
    comment: Union[str, None]
    folderId: Union[str, None]
    folder: Union[DriveFolder, None]
    userId: Union[str, None]
    user: Union[User, None]