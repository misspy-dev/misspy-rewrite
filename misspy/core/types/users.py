
from typing import Union, List, Any

from pydantic import dataclasses
from mitypes import UserLite
from mitypes.user import AvatarDecorations

from .federation import Instance, Emojis, BadgeRoles, field
from .page import Page
from .role import RoleLite
from .note import Note
from .other import Announcement, Achievements, RolePolicies, SecurityKeysList

@dataclasses.dataclass()
class DriveUsage:
    byte: int
    kilobyte: int
    megabyte: int
    gigabyte: int
    terabyte: int

@dataclasses.dataclass()
class UserStat:
    notesCount: int
    repliesCount: int
    renotesCount: int
    repliedCount: int
    renotedCount: int
    pollVotesCount: int
    pollVotedCount: int
    localFollowingCount: int
    remoteFollowingCount: int
    localFollowersCount: int
    remoteFollowersCount: int
    followingCount: int
    followersCount: int
    sentReactionsCount: int
    recivedReactionsCount: int
    noteFavoritesCount: int
    pageLikesCount: int
    pageLikedCount: int
    driveFilesCount: int
    driveUsage: DriveUsage

@dataclasses.dataclass()
class Relation:
    id: str
    isFollowing: bool
    hasPnedingFollowRequestFromYou: bool
    hasPendingFollowRequestToYou: bool
    isFollowed: bool
    isBlocking: bool
    isBlocked: bool
    isMuted: bool
    isRenoteMuted: bool

@dataclasses.dataclass()
class MeDetailed:
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

@dataclasses.dataclass()
class UserDetailedNotMe:
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
    role: RoleLite
    twoFactorEnabled: bool = False
    usePasswordLessLogin: bool = False
    securityKeys: bool = False

@dataclasses.dataclass()
class followers:
    id: str
    createdAt: str
    followeeId: str
    followerId: str
    followee: UserDetailedNotMe
    follower: UserDetailedNotMe

@dataclasses.dataclass()
class reactions:
    id: str
    createdAt: str
    user: UserLite
    type: str

@dataclasses.dataclass()
class Frequently_replied:
    user: Union[UserDetailedNotMe, MeDetailed]
    weight: int

@dataclasses.dataclass()
class Follow:
    id: str
    name: Union[str, None]
    username: str
    host: Union[str, None]
    avatarUrl: Union[str, None]
    avatarBlurhash: Union[str, None]
    avatarDecorations: List[AvatarDecorations]
    isBot: bool
    isCat: bool
    instance: Instance
    emojis: Emojis
    onlineStatus: str
    badgeRoles: BadgeRoles