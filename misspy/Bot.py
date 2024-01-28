import asyncio
from typing import Union

from .core.websocket import MiWS_V2

from .core.types import parser
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
        self.engine = MiWS_V2
        self.ssl = Option.ssl
        self.ext = extension

    def run(self, reconnect=False):
        self.ws = Option.ws_engine(self.address, self.i, self.handler, reconnect, self.ssl)
        asyncio.run(self.ws.start())

    async def handler(self, json: dict):
        if json["type"] == "channel":
            if json["type"] == "note":
                object = await parser.parse_note(json["body"]["body"])
                await extension.exts["note"](object)