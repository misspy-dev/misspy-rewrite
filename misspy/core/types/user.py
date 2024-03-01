from typing import Union

from pydantic import dataclasses

@dataclasses.dataclass
class avatarDecorations:
    id: str
    url: str
    angle: int
    flipH: bool

@dataclasses.dataclass
class User:
    id: str
    createdAt: str
    username: str
    host: Union[str, None]
    name: Union[str, None]
    avatarUrl: Union[str, None]
    avatarBlurhash: Union[str, None]
    avatarDecorations: list[Union[avatarDecorations, None]]
    isAdmin: bool
    isModerator: bool
    isBot: bool
    isCat: bool
    onlineStatus: Union[str, None]

@dataclasses.dataclass
class UserLite:
    id: str
    name: Union[str, None]
    username: str
    host: Union[str, None]
    avatarUrl: Union[str, None]
    avatarBlurhash: Union[str, None]
    avatarDecorations: list[Union[avatarDecorations, None]]
    isAdmin: bool
    isModerator: bool
    isBot: bool
    isCat: bool
    onlineStatus: Union[str, None]