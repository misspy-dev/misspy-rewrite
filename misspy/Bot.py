import asyncio
from typing import Union
import logging
import re

from .core.http import AsyncHttpHandler
from .core.types.note import Note
from .endpoints.drive import drive
from .endpoints.notes import notes
from .settings import Option, extension


class Bot:
    def __init__(
        self,
        address: str,
        i: Union[str, None]
    ) -> None:
        logger = logging.getLogger("misspy")
        self.address = address
        self.i = i
        self.ssl = Option.ssl
        self.ext = extension
        self.http = AsyncHttpHandler(self.address, self.i, self.ssl)

        self.endpoint_list = self.endpoints()
        # ---------- endpoints ------------
        self.notes = notes(self.address, self.i, self.ssl, endpoints=self.endpoint_list)
        self.drive = drive(self.address, self.i, self.ssl, endpoints=self.endpoint_list)
        # ---------------------------------

    async def endpoints(self):
        return await self.http.send("endpoints", data={})

    def run(self, reconnect=False):
        self.ws = Option.ws_engine(
            self.address, self.i, self.handler, reconnect, self.ssl
        )
        asyncio.run(self.ws.start())

    async def connect(self, channel, id=None):
        await self.ws.connect_channel(channel, id)

    async def handler(self, json: dict):
        if json["type"] == "channel":
            if json["body"]["type"] == "note":
                pnote = Note(**json["body"]["body"])
                for func in extension.exts["note"]:
                    await func(pnote)
            if json["body"]["type"] == "followed":
                for func in extension.exts["followed"]:
                    await func()
        elif json["type"] == "__internal":
            if json["body"]["type"] == "ready":
                for func in extension.exts["ready"]:
                    await func()
