from mitypes import User
from mitypes.drive import DriveFile

from ..utils.internaltool import nonecheck
from ..core.http import AsyncHttpHandler, HttpHandler
from ..core.types.favorites import favorite
from ..core.types.likes import GalleryPost, Like
from ..core.types.notifications import notifications as notify
from ..core.types.page import Page, likes
from ..core.types.note import Pin
from ..core.types.blocking import blocking_list
from ..core.types.antennas import created_antnna, show_antnna, notes
from ..core.types.mute import mute as mp_mute
from ..core.types.clip import clips

class i:
    
    def __init__(self, address, i, ssl=True) -> None:
        self.i = i
        self.address = address
        self.ssl = ssl
        self.async_http = AsyncHttpHandler(address, i, ssl)
        
    async def get(self):
        r = await self.async_http.send("i", {})
        return User(**r)

    async def favorites(self, limit=10, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return [favorite(**fav) for fav in await self.async_http.send("i/favorites", base)]

    async def gallery_likes(self, limit=10, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        resp = await self.async_http.send("i/gallery/likes", base)
        likes = []
        for like in resp:
            like["post"]["files"] = [DriveFile(**fav) for fav in resp["files"]]
            likes.append(Like(**like))
        return likes

    async def gallery_posts(self, limit=10, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        resp = await self.async_http.send("i/gallery/posts", base)
        posts = []
        for post in resp:
            post["files"] = [DriveFile(**fav) for fav in resp["files"]]
            posts.append(GalleryPost(**post))
        return posts

    async def notifications(
        self,
        limit=10,
        sinceId=None,
        untilId=None,
        following=False,
        unreadOnly=False,
        markAsRead=True,
        includeTypes=None,
        excludeTypes=None,
    ):
        base = {
            "limit": limit,
            "following": following,
            "unreadOnly": unreadOnly,
            "markAsRead": markAsRead,
        }
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        if nonecheck(includeTypes):
            base["includeTypes"] = includeTypes
        if nonecheck(excludeTypes):
            base["excludeTypes"] = excludeTypes
        return [notify(**notif) for notif in await self.async_http.send("i/notifications", base)]

    async def page_likes(self, limit=10, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return [Page(**page_like) for page_like in await self.async_http.send("i/page-likes", base)]

    async def pages(self, limit=10, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        resp = await self.async_http.send("i/page-likes", base)
        lks = []
        for page_like in resp:
            lks.append(likes(**page_like))
        return lks
    
    async def pin(self, noteId):
        return Pin(
            **await self.async_http.send("i/pin", {"noteId": noteId})
        )

    async def unpin(self, noteId):
        return Pin(
            **await self.async_http.send("i/unpin", {"noteId": noteId})
        )

    async def update(self, params):
        return Pin(**await self.async_http.send("i/update", params))


    async def read_all_unread_notes(self):
        return await self.async_http.send("i/read-all-unread-notes", {})

    async def read_announcement(self, announcementId):
        return await self.async_http.send(
            "i/read-all-unread-notes",
            {"announcementId": announcementId},
        )
    
    
class blocking:
    
    def __init__(self, address, i, ssl=True) -> None:
        self.i = i
        self.address = address
        self.async_http = AsyncHttpHandler(address, i, ssl)

    async def create(self, userId: str):
        params = {"userId": userId}
        r = await self.async_http.send("blocking/create", params)
        return Pin(**r)

    async def delete(self, userId: str):
        params = {"userId": userId}
        r = await self.async_http.send("blocking/delete", params)
        return r

    async def list(
        self, limit: int = 30, sinceId: str = None, untilId: str = None
    ):
        params = {
            "limit": limit,
        }
        if sinceId is not None:
            params["sinceId"] = sinceId
        if untilId is not None:
            params["untilId"] = untilId
        r = await self.async_http.send("blocking/list", params)
        return [blocking_list(**page_like) for page_like in r]

class antennas:
    
    def __init__(self, address, i, ssl=True) -> None:
        self.i = i
        self.address = address
        self.async_http = AsyncHttpHandler(address, i, ssl)
        
    async def create(
        self,
        name,
        src,
        keywords,
        excludeKeywords,
        users,
        caseSensitive,
        withReplies,
        withFile,
        notify,
        userListId=None,
    ):
        base = {
            "name": name,
            "src": src,
            "keywords": keywords,
            "excludeKeywords": excludeKeywords,
            "users": users,
            "caseSensitive": caseSensitive,
            "withReplies": withReplies,
            "withFile": withFile,
            "notify": notify,
        }
        if nonecheck(userListId):
            base["userListId"] = userListId
        return created_antnna(**await self.async_http.send("antennas/create", base))

    async def update(
        self,
        name,
        src,
        keywords,
        excludeKeywords,
        users,
        caseSensitive,
        withReplies,
        withFile,
        notify,
        userListId=None,
    ):
        base = {
            "name": name,
            "src": src,
            "keywords": keywords,
            "excludeKeywords": excludeKeywords,
            "users": users,
            "caseSensitive": caseSensitive,
            "withReplies": withReplies,
            "withFile": withFile,
            "notify": notify,
        }
        if nonecheck(userListId):
            base["userListId"] = userListId
        return created_antnna(**self.async_http.send("antennas/update", base))

    async def delete(self, antennaId):
        return self.async_http.send("antennas/delete", {"antennaId": antennaId})

    async def show(self, antennaId):
        return show_antnna(
            **self.async_http.send("antennas/show", {"antennaId": antennaId})
        )

    async def list(self):
        return [show_antnna(**r) for r in await self.async_http.send("antennas/list", {})]

    async def notes(
        self,
        antennaId,
        limit=10,
        sinceId=None,
        untilId=None,
        sinceDate=None,
        untilDate=None,
    ):
        base = {"antennaId": antennaId, "limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        if nonecheck(sinceDate):
            base["sinceDate"] = sinceDate
        if nonecheck(untilDate):
            base["untilDate"] = untilDate
        return [notes(**r) for r in await self.async_http.send("antennas/notes", base)]


class mute:
    
    def __init__(self, address, i, ssl=True) -> None:
        self.i = i
        self.address = address
        self.async_http = AsyncHttpHandler(address, i, ssl)

    async def create(self, userId, expiresAt=None):
        return await self.async_http.send(
                "mute/create",
                {"userId": userId, "expiresAt": expiresAt},
            )

    async def list(self, limit=30, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return [mp_mute(**r) for r in await self.async_http.send("mute/list", base)]

    async def delete(self, userId):
        return await self.async_http.send("mute/delete", {"userId": userId})

class users:
    
    def __init__(self, address, i, ssl=True) -> None:
        self.i = i
        self.address = address
        self.http = AsyncHttpHandler(address, i, ssl)
        self.http_sync = HttpHandler(address, i, ssl)
        
    async def get(
        self, limit=10, offset=0, sort=None, state="all", origin="local", hostname=None
    ):
        base = {
            "limit": limit,
            "offset": offset,
            "state": state,
            "origin": origin,
            "hostname": hostname,
        }
        if nonecheck(sort):
            base["sort"] = sort
        return [Pin(**r) for r in await self.http.send("users", base)]

    async def users_clips(self, userId, limit=10, sinceId=None, untilId=None):
        base = {"userId": userId, "limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return [clips(**r) for r in await self.http.send("users/clips", base)]
 
    async def users_followers(self, limit=10, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return AttrDict(await self.async_http.send("users/followers", base))

    async def users_following(self, limit=10, sinceId=None, untilId=None):
        base = {"limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return AttrDict(await self.async_http.send("users/following", base))

    async def users_gallery_posts(self, userId, limit=10, sinceId=None, untilId=None):
        base = {"userId": userId, "limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return AttrDict(
            await self.async_http.send("users/gallery/posts", base)
        )

    async def users_pages(self, userId, limit=10, sinceId=None, untilId=None):
        base = {"userId": userId, "limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return AttrDict(await self.async_http.send("users/pages", base))

    async def users_reactions(
        self,
        userId,
        limit=10,
        sinceId=None,
        untilId=None,
        sinceDate=None,
        untilDate=None,
    ):
        base = {"userId": userId, "limit": limit}
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        if nonecheck(sinceDate):
            base["sinceDate"] = sinceDate
        if nonecheck(untilDate):
            base["untilDate"] = untilDate
        return AttrDict(await self.async_http.send("users/reactions", base))

    async def users_recommendation(
        self,
        limit=10,
        offset=0,
    ):
        base = {"limit": limit, "offset": offset}
        return AttrDict(
            await self.async_http.send("users/recommendation", base)
        )

    async def users_relation(self, userId):
        return AttrDict(
            await self.async_http.send("users/relation", {"userId": userId})
        )

    async def users_report_abuse(self, userId, comment):
        return AttrDict(
            await self.async_http.send(
                "users/report-abuse",
                {"userId": userId, "comment": comment},
            )
        )

    async def users_search_by_username_and_host(
        self, username=None, host=None, limit=10, detail=True
    ):
        return AttrDict(
            await self.async_http.send(
                "users/search-by-username-and-host",
                {"username": username, "host": host, "limit": limit, "detail": detail},
            )
        )

    async def users_search(
        self, query, offset=0, limit=10, origin="combined", detail=True
    ):
        return AttrDict(
            await self.async_http.send(
                "users/search",
                {
                    "query": query,
                    "offset": offset,
                    "limit": limit,
                    "origin": origin,
                    "detail": detail,
                },
            )
        )

    def users_show(self, username, host=None):
        d = self.http.send(
            "users/show", {"username": username, "host": None}
        )
        return AttrDict(d)

    async def users_stats(self, userId):
        return AttrDict(
            await self.async_http.send("users/stats", {"userId": userId})
        )

    async def users_get_frequently_replied_users(
        self,
        userId,
        limit=10,
    ):
        base = {"userId": userId, "limit": limit}
        return AttrDict(
            await self.async_http.send(
                "users/get-frequently-replied-users", base
            )
        )

    async def users_notes(
        self,
        userId,
        includeReplies=True,
        limit=10,
        sinceId=None,
        untilId=None,
        sinceDate=None,
        untilDate=None,
        includeMyRenotes=True,
        withFiles=False,
        fileType=None,
        excludeNsfw=False,
    ):
        base = {
            "userId": userId,
            "includeReplies": includeReplies,
            "limit": limit,
            "includeMyRenotes": includeMyRenotes,
            "withFiles": withFiles,
            "excludeNsfw": excludeNsfw,
        }
        if nonecheck(sinceDate):
            base["sinceDate"] = sinceDate
        if nonecheck(untilDate):
            base["untilDate"] = untilDate
        if nonecheck(withFiles):
            base["withFiles"] = withFiles
        if nonecheck(fileType):
            base["fileType"] = fileType
        if nonecheck(sinceId):
            base["sinceId"] = sinceId
        if nonecheck(untilId):
            base["untilId"] = untilId
        return AttrDict(await self.async_http.send("users/notes", base))
    
class following:
    
    def __init__(self, address, i, ssl=True) -> None:
        self.i = i
        self.address = address
    
    async def create(self, userId):
        return AttrDict(
            await self.async_http.send(
                "following/create", {"userId": userId}
            )
        )

    async def delete(self, userId):
        return AttrDict(
            await self.async_http.send(
                "following/delete", {"userId": userId}
            )
        )

    async def invalidate(self, userId):
        return AttrDict(
            await self.async_http.send(
                "following/invalidate", {"userId": userId}
            )
        )

    async def requests_accept(self, userId):
        return AttrDict(
            await self.async_http.send(
                "following/requests/accept", {"userId": userId}
            )
        )

    async def requests_cancel(self, userId):
        return AttrDict(
            await self.async_http.send(
                "following/requests/cancel", {"userId": userId}
            )
        )

    async def requests_list(self):
        return AttrDict(
            await self.async_http.send("following/requests/list", {})
        )

    async def requests_reject(self, userId):
        return AttrDict(
            await self.async_http.send(
                "following/requests/reject", {"userId": userId}
            )
        )