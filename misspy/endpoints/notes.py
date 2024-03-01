from typing import List, Union

from ..__init__ import visibility
from ..core.http import AsyncHttpHandler
from ..core.types.note import Note
from ..core.types.poll import Poll


class notes:
    def __init__(self, address, i, ssl) -> None:
        self.http = AsyncHttpHandler(address, i, ssl)

    async def create(
        self,
        text: Union[str, None] = None,
        visibility: str = visibility.public,
        visibleUserIds: List[str] = [],
        cw: Union[str, None] = None,
        localOnly: bool = False,
        noExtractMentions: bool = False,
        noExtractHashtags: bool = False,
        noExtractEmojis: bool = False,
        fileIds: List[str] = [],
        replyId: Union[str, None] = None,
        renoteId: Union[str, None] = None,
        channelId: Union[str, None] = None,
        poll: Union[Poll, None] = None,
    ) -> Note:
        """Create a post. Replies and Renotes are also made using this function.

        Args:
            text (Union[str, None], optional): The text of the post. Defaults to None.
            visibility (str, optional): Publication range of posts. Defaults to visibility.public.
            visibleUserIds (List[str], optional): A list of user IDs that can view the post. Applies only when visibility is 'specified'.
            cw (Union[str, None], optional): CW (Content Warning) of the post. Defaults to None.
            localOnly (bool, optional): If set to True, posts will only be posted locally. Defaults to False.
            noExtractMentions (bool, optional): If set to True, mentions will not be expanded from the body. Defaults to False.
            noExtractHashtags (bool, optional): If set to True, hashtags will not be expanded from the body. Defaults to False.
            noExtractEmojis (bool, optional): If set to True, emojis will not be expanded from the body. Defaults to False.
            fileIds (List[str], optional): The id of the file to attach to the post.
            replyId (Union[str, None], optional): The id of the post to reply to. Defaults to None.
            renoteId (Union[str, None], optional): ID of the post targeted for Renote. Defaults to None.
            channelId (Union[str, None], optional): ID of the channel to post to. Defaults to None.
            poll (Union[Poll, None], optional): Voting parameters. Defaults to None.

        Returns:
            Note: created Post.
        """
        data = {
            "text": text,
            "visibility": visibility,
            "visibleUserIds": visibleUserIds,
            "cw": cw,
            "localOnly": localOnly,
            "noExtractMentions": noExtractMentions,
            "noExtractHashtags": noExtractHashtags,
            "noExtractEmojis": noExtractEmojis,
            "fileIds": fileIds,
            "replyId": replyId,
            "renoteId": renoteId,
            "channelId": channelId,
            "poll": poll
        }
        return Note(**await self.http.send("notes/create", data=data))