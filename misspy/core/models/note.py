import sys
from datetime import datetime
from typing import Any, List, Union

from mitypes.drive import DriveFile
from mitypes.user import AvatarDecorations, UserLite
from pydantic.dataclasses import dataclass, Field
from pydantic import JsonValue

from .action import APIAction
from .channel import Channel
from .federation import BadgeRoles, Emojis, Instance
from .internal import mspy
from .other import Achievements, Announcement, RolePolicies, SecurityKeysList
from .page import Page
from .role import RoleLite


@dataclass()
class Context:
    id: str
    createdAt: str
    userId: str
    user: UserLite
    localOnly: bool
    renoteCount: int
    repliesCount: int
    clippedCount: int
    reactionCount: int
    reactionEmojis: dict
    reactionAndUserPairCache: List[str]
    replyId: Union[str, None] = None
    renoteId: Union[str, None] = None
    visibility: str = None
    reactions: Union[dict, None] = None
    uri: Union[str, None] = None
    url: Union[str, None] = None
    isHidden: Union[bool, None] = None
    deletedAt: Union[str, None] = None
    text: Union[str, None] = None
    cw: Union[str, None] = None
    reply: Union[dict, None] = None
    renote: Union[dict, None] = None
    mentions: List[str] = Field(default_factory=list)
    visibleUserIds: List[str] = Field(default_factory=list)
    fileIds: List[str] = Field(default_factory=list)
    files: List[DriveFile] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    poll: Union[dict, None] = None
    channelId: Union[str, None] = None
    channel: Union[dict, None] = None
    reactionAcceptance: Union[str, None] = None
    reactionAndUserPairCache: List[str] = Field(default_factory=list)
    misspy: Union[mspy, None] = None
    api: Union[APIAction, None] = None


@dataclass()
class Note:
    id: str
    createdAt: str
    userId: str
    user: UserLite
    visibility: str
    localOnly: bool
    uri: str
    url: str
    reactions: dict
    renoteCount: int
    repliesCount: int
    reactionCount: int
    clippedCount: int
    reactionEmojis: dict
    reactionAndUserPairCache: List[str]
    replyId: Union[str, None] = None
    renoteId: Union[str, None] = None
    myReaction: Union[dict, None] = None

    isHidden: Union[bool, None] = None
    deletedAt: Union[str, None] = None
    text: Union[str, None] = None
    cw: Union[str, None] = None
    reply: Union[dict, None] = None
    renote: Union[dict, None] = None
    mentions: List[str] = Field(default_factory=list)
    visibleUserIds: List[str] = Field(default_factory=list)
    fileIds: List[str] = Field(default_factory=list)
    files: List[DriveFile] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    poll: Union[dict, None] = None
    channelId: Union[str, None] = None
    channel: Union[Channel, None] = None
    reactionAcceptance: Union[str, None] = None
    reactionAndUserPairCache: List[str] = Field(default_factory=list)
    misspy: Union[mspy, None] = None

    def __post_init__(self):
        verinf = sys.version_info
        if not verinf.major + verinf.minor >= 311:
            self.createdAt = datetime.fromisoformat(
                self.createdAt.replace("Z", "+00:00")
            )
            if self.deletedAt:
                self.deletedAt = datetime.fromisoformat(
                    self.deletedAt.replace("Z", "+00:00")
                )
        else:
            self.createdAt = datetime.fromisoformat(self.createdAt)
            if self.deletedAt:
                self.deletedAt = datetime.fromisoformat(self.deletedAt)

"""
@dataclass()
class Pin:
    id: str
    createdAt: str
    isLocked: bool
    isSilenced: bool
    isLimited: bool
    isSuspended: bool
    followersCount: int
    followingCount: int
    notesCount: int
    pinnedPage: Page
    publicReactions: bool
    followingVisibility: str
    followersVisibility: str
    moderationNote: str
    isFollowing: bool
    isFollowed: bool
    hasPendingFollowRequestFromYou: bool
    hasPendingFollowRequestToYou: bool
    isBlocking: bool
    isBlocked: bool
    isMuted: bool
    isRenoteMuted: bool
    notify: str
    withReplies: bool
    injectFeaturedNote: bool
    receiveAnnouncementEmail: bool
    alwaysMarkNsfw: bool
    autoSensitive: bool
    carefulBot: bool
    autoAcceptFollowed: bool
    noCrawle: bool
    preventAiLearning: bool
    isExplorable: bool
    isDeleted: bool
    twoFactorBackupCodesStock: str
    hideOnlineStatus: bool
    hasUnreadSpecifiedNotes: bool
    hasUnreadMentions: bool
    hasUnreadAnnouncement: bool
    unreadAnnouncements: List[Announcement]
    hasUnreadAntenna: bool
    hasUnreadChannel: bool
    hasUnreadNotification: bool
    hasPendingReceivedFollowRequest: bool
    unreadNotificationsCount: int
    notificationRecieveConfig: Any
    loggedInDays: int
    policies: RolePolicies
    role: RoleLite
    name: Union[str, None] = None
    username: Union[str, None] = None
    host: Union[str, None] = None
    avatarUrl: Union[str, None] = None
    avatarBlurhash: Union[str, None] = None
    avatarDecorations: List[AvatarDecorations] = Field(default_factory=list)
    isBot: Union[bool, None] = None
    isCat: Union[bool, None] = None
    instance: Union[Instance, None] = None
    emojis: Emojis = Field(default_factory=list)
    onlineStatus: str = Field(default_factory="unknown")
    badgeRoles: List[BadgeRoles] = Field(default_factory=list)
    url: Union[str, None] = None
    uri: Union[str, None] = None
    movedTo: Union[str, None] = None
    alsoKnownAs: List[Union[str, None]] = None
    updatedAt: Union[str, None] = None
    lastFetchedAt: Union[str, None] = None
    bannerUrl: Union[str, None] = None
    bannerBlurhash: Union[str, None] = None
    description: Union[str, None] = None
    location: Union[str, None] = None
    birthday: Union[str, None] = None
    lang: Union[str, None] = None
    Fields: List[Field] = Field(default_factory=list)
    verifiedLinks: List[str] = Field(default_factory=list)
    pinnedNoteIds: List[str] = Field(default_factory=list)
    pinnedNotes: List[Note] = Field(default_factory=list)
    pinnedPageId: Union[str, None] = None
    memo: Union[str, None] = None

    avatarId: Union[str, None] = None
    bannerId: Union[str, None] = None
    isModerator: Union[bool, None] = None
    isAdmin: Union[bool, None] = None

    mutedWords: List[str] = Field(default_factory=list)
    mutedInstances: List[Union[str, None]] = None
    emailNotificationTypes: List[str] = Field(default_factory=list)
    achievements: List[Achievements] = Field(default_factory=list)

    email: Union[str, None] = None
    emailVerified: Union[bool, None] = None
    securityKeysList: List[SecurityKeysList] = Field(default_factory=list)
    twoFactorEnabled: bool = False
    usePasswordLessLogin: bool = False
    securityKeys: bool = False
"""