from typing import Union, List, Any
from mitypes.user import AvatarDecorations

from pydantic import dataclasses, Field

from mitypes.user import UserLite
from mitypes.drive import DriveFile

from .internal import mspy
from .action import APIAction
from .page import Page
from .federation import Instance, Emojis, BadgeRoles, field
from .role import RoleLite

@dataclasses.dataclass(config=dict(extra="allow"))
class Context:
    id: str
    createdAt: str
    userId: str
    user: UserLite
    replyId: Union[str, None]
    renoteId: Union[str, None]
    visibility: str
    localOnly: bool

    reactions: Union[dict, None] = None
    myReaction: Union[dict, None] = None
    uri: Union[str, None] = None
    url: Union[str, None] = None
    renoteCount: Union[int, None] = None
    replyesCount: Union[int, None] = None
    isHidden: Union[bool, None] = None
    deletedAt: Union[str, None] = None
    text: Union[str, None] = None
    cw: Union[str, None] = None
    reply: Union[dict, None] = None
    renote: Union[dict, None] = None
    mentions: List[str] = Field(default_factory=List)
    visibleUserIds: List[str] = Field(default_factory=List)
    fileIds: List[str] = Field(default_factory=List)
    files: List[DriveFile] = Field(default_factory=List)
    tags: List[str] = Field(default_factory=List)
    poll: Union[dict, None] = None
    channelId: Union[str, None] = None
    channel: Union[dict, None] = None
    reactionAcceptance: Union[str, None] = None
    reactionAndUserPairCache: List[str] = Field(default_factory=List)
    misspy: Union[mspy, None] = None
    api: Union[APIAction, None] = None

@dataclasses.dataclass(config=dict(extra="allow"))
class Note:
    id: str
    createdAt: str
    userId: str
    user: UserLite
    replyId: Union[str, None]
    renoteId: Union[str, None]
    visibility: str
    localOnly: bool
    reactions: Union[dict, None] = None
    myReaction: Union[dict, None] = None
    uri: Union[str, None] = None
    url: Union[str, None] = None
    renoteCount: Union[int, None] = None
    replyesCount: Union[int, None] = None
    isHidden: Union[bool, None] = None
    deletedAt: Union[str, None] = None
    text: Union[str, None] = None
    cw: Union[str, None] = None
    reply: Union[dict, None] = None
    renote: Union[dict, None] = None
    mentions: List[str] = Field(default_factory=List)
    visibleUserIds: List[str] = Field(default_factory=List)
    fileIds: List[str] = Field(default_factory=List)
    files: List[DriveFile] = Field(default_factory=List)
    tags: List[str] = Field(default_factory=List)
    poll: Union[dict, None] = None
    channelId: Union[str, None] = None
    channel: Union[dict, None] = None
    reactionAcceptance: Union[str, None] = None
    reactionAndUserPairCache: List[str] = Field(default_factory=List)
    misspy: Union[mspy, None] = None



@dataclasses.dataclass()
class SecurityKeysList:
    id: str
    name: str
    lastUsed: str

@dataclasses.dataclass()
class RolePolicies:
    gtlAvailable: bool
    ltlAvailable: bool
    canPublicNote: bool
    canInitiateConversation: bool
    canCreateContent: bool
    canUpdateContent: bool
    canDeleteContent: bool
    canPurgeAccount: bool
    canUpdateAvatar: bool
    canUpdateBanner: bool
    mentionLimit: int
    canInvite: bool
    inviteLimit: int
    inviteLimitCycle: int
    inviteExpirationTime: int
    canManageCustomEmojis: bool
    canManageAvatarDecorations: bool
    canSearchNotes: bool
    canUseTranslator: bool
    canUseDriveFileInSoundSettings: bool
    canHideAds: bool
    driveCapacityMb: int
    alwaysMarkNsfw: bool
    skipNsfwDetection: bool
    pinLimit: int
    antennaLimit: int
    antennaNotesLimit: int
    wordMuteLimit: int
    webhookLimit: int
    clipLimit: int
    noteEachClipsLimit: int
    userListLimit: int
    userEachUserListsLimit: int
    rateLimitFactor: int
    avatarDecorationLimit: int

@dataclasses.dataclass()
class Achievements:
    name: str
    unlockedAt: int

@dataclasses.dataclass()
class Announcement:
    id: str
    createdAt: str
    updatedAt: Union[str, None]
    text: str
    title: str
    imageUrl: Union[str, None]
    icon: str
    display: str
    needConfirmationToRead: bool
    forYou: bool
    closeDuration: int
    displayOrder: int
    silence: bool
    isRead: bool

@dataclasses.dataclass()
class Pin:
    id: str
    name: Union[str, None]
    username: str
    host: Union[str, None]
    avatarUrl: Union[str, None]
    avatarBlurhash: Union[str, None]
    avatarDecorations: AvatarDecorations
    isBot: bool
    isCat: bool
    instance: Instance
    emojis: Emojis
    onlineStatus: str
    badgeRoles: List[BadgeRoles]
    url: Union[str, None]
    uri: Union[str, None]
    movedTo: Union[str, None]
    alsoKnownAs: List[Union[str, None]]
    createdAt: str
    updatedAt: Union[str, None]
    lastFetchedAt: Union[str, None]
    bannerUrl: Union[str, None]
    bannerBlurhash: Union[str, None]
    isLocked: bool
    isSilenced: bool
    isLimited: bool
    isSuspended: bool
    description: Union[str, None]
    location: Union[str, None]
    birthday: Union[str, None]
    lang: Union[str, None]
    fields: List[field]
    verifiedLinks: List[str]
    followersCount: int
    followingCount: int
    notesCount: int
    pinnedNoteIds: List[str]
    pinnedNotes: List[Note]
    pinnedPageId: Union[str, None]
    pinnedPage: Page
    publicReactions: bool
    followingVisibility: str
    followersVisibility: str
    memo: Union[str, None]
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
    avatarId: Union[str, None]
    bannerId: Union[str, None]
    isModerator: Union[bool, None]
    isAdmin: Union[bool, None]
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
    mutedWords: List[str]
    mutedInstances: List[Union[str, None]]
    notificationRecieveConfig: Any
    emailNotificationTypes: List[str]
    achievements: List[Achievements]
    loggedInDays: int
    policies: RolePolicies
    role: RoleLite
    email: Union[str, None]
    emailVerified: Union[bool, None]
    securityKeysList: List[SecurityKeysList]
    twoFactorEnabled: bool = False
    usePasswordLessLogin: bool = False
    securityKeys: bool = False