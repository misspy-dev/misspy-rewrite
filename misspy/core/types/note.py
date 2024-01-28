import dataclasses
from typing import Union

from .user import User, UserLite
from .drive import DriveFile

@dataclasses.dataclass
class visibility:
    public = "public"
    home = "home"
    followers = "followers"
    specified = "specified"

@dataclasses.dataclass
class Note:
    id: str
    createdAt: str
    deletedAt: Union[str, None]
    text: Union[str, None]
    cw: Union[str, None]
    userId: str
    user: UserLite
    replyId: str
    renoteId: str
    reply: Union[dict, None]
    renote: Union[dict, None]
    isHidden: bool
    visibility: str
    mentions: list[str]
    visibleUserIds: list[str]
    fileIds: list[str]
    files: list[DriveFile]
    tags: list[str]
    poll: Union[dict, None]
    channelId: Union[str, None]
    channel: Union[dict, None]
    localOnly: bool
    reactionAcceptance: Union[str, None]
    reactions: dict
    renoteCount: int
    replyesCount: int
    uri: str
    url: str
    reactionAndUserPairCache: list[str]
    myReaction: dict