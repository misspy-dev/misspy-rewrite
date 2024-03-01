import asyncio
from typing import Union

from .core.types.note import Note
from .settings import Option
from .settings import extension


class Bot:
    def __init__(
        self,
        address: str,
        i: Union[str, None],
    ) -> None:
        self.address = address
        self.i = i
        self.ssl = Option.ssl
        self.ext = extension

    def run(self, reconnect=False):
        self.ws = Option.ws_engine(self.address, self.i, self.handler, reconnect, self.ssl)
        asyncio.run(self.ws.start())

    async def connect(self, channel, id=None):
        await self.ws.connect_channel(channel, id)

    async def handler(self, json: dict):
        if json["type"] == "channel":
            if json["body"]["type"] == "note":
                pnote = Note(**json["body"]["body"])
                for func in extension.exts["note"]:
                    await func(pnote)
            if json['body']['type'] == 'followed':
                for func in extension.exts["followed"]:
                    await func()
        elif json["type"] == "__internal":
            if json["body"]["type"] == "ready":
                for func in extension.exts["ready"]:
                    await func()