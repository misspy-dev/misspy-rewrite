from typing import List, Union

from mitypes.drive import DriveFile
from mitypes.user import UserLite
from pydantic import Field, dataclasses

from .action import APIAction
from .channel import Channel
from .internal import mspy


@dataclasses.dataclass(config=dict(extra="allow"))
class Context:
    id: str
    createdAt: str
    userId: str
    user: UserLite
    replyId: Union[str, None] = Field(default_factory=None)
    renoteId: Union[str, None] = Field(default_factory=None)
    visibility: str
    localOnly: bool
    reactions: Union[dict, None] = Field(default_factory=None)
    myReaction: Union[dict, None] = Field(default_factory=None)
    uri: Union[str, None] = Field(default_factory=None)
    url: Union[str, None] = Field(default_factory=None)
    renoteCount: Union[int, None] = Field(default_factory=None)
    replyesCount: Union[int, None] = Field(default_factory=None)
    isHidden: Union[bool, None] = Field(default_factory=None)
    deletedAt: Union[str, None] = Field(default_factory=None)
    text: Union[str, None] = Field(default_factory=None)
    cw: Union[str, None] = Field(default_factory=None)
    reply: Union[dict, None] = Field(default_factory=None)
    renote: Union[dict, None] = Field(default_factory=None)
    mentions: List[str] = Field(default_factory=List)
    visibleUserIds: List[str] = Field(default_factory=List)
    fileIds: List[str] = Field(default_factory=List)
    files: List[DriveFile] = Field(default_factory=List)
    tags: List[str] = Field(default_factory=List)
    poll: Union[dict, None] = Field(default_factory=None)
    channelId: Union[str, None] = Field(default_factory=None)
    channel: Union[dict, None] = Field(default_factory=None)
    reactionAcceptance: Union[str, None] = Field(default_factory=None)
    reactionAndUserPairCache: List[str] = Field(default_factory=List)
    misspy: Union[mspy, None] = Field(default_factory=None)
    api: Union[APIAction, None] = Field(default_factory=None)


@dataclasses.dataclass(config=dict(extra="allow"))
class Note:
    id: str
    createdAt: str
    userId: str
    user: UserLite
    replyId: Union[str, None] = Field(default_factory=None)
    renoteId: Union[str, None] = Field(default_factory=None)
    visibility: str
    localOnly: bool
    reactions: Union[dict, None] = Field(default_factory=None)
    myReaction: Union[dict, None] = Field(default_factory=None)
    uri: Union[str, None] = Field(default_factory=None)
    url: Union[str, None] = Field(default_factory=None)
    renoteCount: Union[int, None] = Field(default_factory=None)
    replyesCount: Union[int, None] = Field(default_factory=None)
    isHidden: Union[bool, None] = Field(default_factory=None)
    deletedAt: Union[str, None] = Field(default_factory=None)
    text: Union[str, None] = Field(default_factory=None)
    cw: Union[str, None] = Field(default_factory=None)
    reply: Union[dict, None] = Field(default_factory=None)
    renote: Union[dict, None] = Field(default_factory=None)
    mentions: List[str] = Field(default_factory=List)
    visibleUserIds: List[str] = Field(default_factory=List)
    fileIds: List[str] = Field(default_factory=List)
    files: List[DriveFile] = Field(default_factory=List)
    tags: List[str] = Field(default_factory=List)
    poll: Union[dict, None] = Field(default_factory=None)
    channelId: Union[str, None] = Field(default_factory=None)
    channel: Union[Channel, None] = Field(default_factory=None)
    reactionAcceptance: Union[str, None] = Field(default_factory=None)
    reactionAndUserPairCache: List[str] = Field(default_factory=List)
    misspy: Union[mspy, None] = Field(default_factory=None)


"""
@dataclasses.dataclass()
class Pin:
    id: str
    name: Union[str, None] = Field(default_factory=None)
    username: Union[str, None] = Field(default_factory=None)
    host: Union[str, None] = Field(default_factory=None)
    avatarUrl: Union[str, None] = Field(default_factory=None)
    avatarBlurhash: Union[str, None] = Field(default_factory=None)
    avatarDecorations: List[AvatarDecorations] = Field(default_factory=List)
    isBot: Union[bool, None] = Field(default_factory=None)
    isCat: Union[bool, None] = Field(default_factory=None)
    instance: Union[Instance, None] = Field(default_factory=None)
    emojis: Emojis = Field(default_factory=List)
    onlineStatus: str = Field(default_factory="unknown")
    badgeRoles: List[BadgeRoles] = Field(default_factory=list)
    url: Union[str, None] = Field(default_factory=None)
    uri: Union[str, None] = Field(default_factory=None)
    movedTo: Union[str, None] = Field(default_factory=None)
    alsoKnownAs: List[Union[str, None]] = Field(default_factory=None)
    createdAt: str
    updatedAt: Union[str, None] = Field(default_factory=None)
    lastFetchedAt: Union[str, None] = Field(default_factory=None)
    bannerUrl: Union[str, None] = Field(default_factory=None)
    bannerBlurhash: Union[str, None] = Field(default_factory=None)
    isLocked: bool
    isSilenced: bool
    isLimited: bool
    isSuspended: bool
    description: Union[str, None] = Field(default_factory=None)
    location: Union[str, None] = Field(default_factory=None)
    birthday: Union[str, None] = Field(default_factory=None)
    lang: Union[str, None] = Field(default_factory=None)
    fields: List[field] = Field(default_factory=list)
    verifiedLinks: List[str] = Field(default_factory=list)
    followersCount: int
    followingCount: int
    notesCount: int
    pinnedNoteIds: List[str] = Field(default_factory=list)
    pinnedNotes: List[Note] = Field(default_factory=list)
    pinnedPageId: Union[str, None] = Field(default_factory=None)
    pinnedPage: Page
    publicReactions: bool
    followingVisibility: str
    followersVisibility: str
    memo: Union[str, None] = Field(default_factory=None)
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
    avatarId: Union[str, None] = Field(default_factory=None)
    bannerId: Union[str, None] = Field(default_factory=None)
    isModerator: Union[bool, None] = Field(default_factory=None)
    isAdmin: Union[bool, None] = Field(default_factory=None)
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
    mutedWords: List[str] = Field(default_factory=list)
    mutedInstances: List[Union[str, None]] = Field(default_factory=None)
    notificationRecieveConfig: Any
    emailNotificationTypes: List[str] = Field(default_factory=list)
    achievements: List[Achievements] = Field(default_factory=list)
    loggedInDays: int
    policies: RolePolicies
    role: RoleLite
    email: Union[str, None] = Field(default_factory=None)
    emailVerified: Union[bool, None] = Field(default_factory=None)
    securityKeysList: List[SecurityKeysList] = Field(default_factory=list)
    twoFactorEnabled: bool = False
    usePasswordLessLogin: bool = False
    securityKeys: bool = False
"""
