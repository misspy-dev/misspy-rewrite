import asyncio
import logging
from functools import partial

# from importlib import import_module
from typing import Union

from mitypes.user import User

from .core.exception import (
    ClientException,
    MisskeyAPIError,
)
from .core.http import AsyncHttpHandler, HttpHandler
from .core.types.internal import error
from .core.types.note import Context
from .endpoints.drive import drive
from .endpoints.notes import notes
from .endpoints.reaction import reactions
from .flags import misspy_flag


class Bot:
    def __init__(self, address: str, i: Union[str, None]) -> None:
        self.apierrors = []
        # self.Flag = misspy_flag()
        self.logger = logging.getLogger("misspy")
        self.address = address
        self.i = i
        self.flag = misspy_flag
        self.ssl = self.flag.ssl
        self.http = AsyncHttpHandler(self.address, self.i, self.ssl, logger=self.logger)
        self.http_sync = HttpHandler(self.address, self.i, self.ssl)
        self.user: User = User(**self.__i())
        self.funcs: dict = {}

        self.endpoint_list = self.endpoints()
        args = {
            "address": self.address,
            "i": self.i,
            "ssl": self.ssl,
            "endpoints": self.endpoint_list,
            "handler": self.http,
        }
        # ---------- endpoints ------------
        self.notes = notes(**args)
        self.drive = drive(**args)
        self.reactions = reactions(**args)
        # ---------------------------------

    def __i(self):
        return self.http_sync.send("i", data={})

    def endpoints(self):
        return self.http_sync.send("endpoints", data={})

    def run(self, reconnect=False):
        asyncio.run(self.start())

    async def start(self, reconnect=False):
        self.ws = self.flag.engine(
            self.address, self.i, self.handler, reconnect, self.ssl
        )
        await self.handler({"type": "__internal", "body": {"type": "setup_hook"}})
        await self.ws.start()

    def event(self, event=""):
        """A decorator that can listen for events in Discord.py-like notation.

        Examples:
        ```python
        @bot.event("ready")
        async def ready():
            print("ready!")
        ```

        Args:
            event (str): Name of the event to listen for.
        """

        def decorator(func):
            func.__event_type = event
            if self.funcs.get(event) and isinstance(self.funcs.get(event), list):
                ev: list = self.funcs.get(event)
                ev.append(func)
            else:
                self.funcs[event] = [func]
            return func

        return decorator

    """
    async def load_extension(self, module: str):
        module = import_module(module)
        try:
            await module.setup(self)
        except AttributeError:
            raise NotExtensionError(
                "Module loading failed because the setup function does not exist in the module."
            )
    """

    async def connect(self, channel, id=None):
        await self.ws.connect_channel(channel, id)

    async def handler(self, json: dict):
        if json["type"] == "channel":
            if json["body"]["type"] == "note":
                if self.funcs.get("note") is None:
                    return
                json["body"]["body"]["api"] = {}
                json["body"]["body"]["api"]["reactions"] = {}
                json["body"]["body"]["api"]["reactions"]["create"] = partial(
                    self.reactions.create, noteId=json["body"]["body"]["id"]
                )
                json["body"]["body"]["api"]["reactions"]["delete"] = partial(
                    self.reactions.delete, noteId=json["body"]["body"]["id"]
                )
                json["body"]["body"]["api"]["reply"] = partial(
                    self.notes.create, replyId=json["body"]["body"]["id"]
                )
                json["body"]["body"]["api"]["renote"] = partial(
                    self.notes.create, renoteId=json["body"]["body"]["id"]
                )
                pnote = Context(**json["body"]["body"])
                for func in self.funcs["note"]:
                    await func(pnote)
            if json["body"]["type"] == "followed":
                if self.funcs.get("note") is None:
                    return
                for func in self.funcs["followed"]:
                    await func()
        elif json["type"] == "__internal":
            if json["body"]["type"] == "setup_hook":
                if self.funcs.get("setup_hook") is None:
                    return
                for func in self.funcs["setup_hook"]:
                    await func()
            if json["body"]["type"] == "ready":
                if self.funcs.get("ready") is None:
                    return
                for func in self.funcs["ready"]:
                    await func()
            elif json["body"]["type"] == "exception":
                if self.funcs.get("error"):
                    eb = {
                        "type": json["body"]["errorType"],
                        "exc": json["body"]["exc"],
                        "exc_obj": json["body"]["exc_obj"],
                    }
                    for func in self.funcs["error"]:
                        await func(error(**eb))
                else:
                    if json["body"]["errorType"] in self.apierrors:
                        raise MisskeyAPIError(json["body"]["exc"])
                    else:
                        raise ClientException(json["body"]["exc"])
