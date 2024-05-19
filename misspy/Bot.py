import asyncio
import inspect
import logging
import traceback
from enum import Enum
from functools import partial

# from importlib import import_module
from typing import Union

from mitypes.user import User

from .core.exception import (
    ClientException,
    MisskeyAPIError,
)

#     NotExtensionError
from .core.http import AsyncHttpHandler, HttpHandler
from .core.models.internal import error
from .core.models.note import Context
from .core.websocket import MiWS_V2

# from .core.models.note import Context
from .endpoints.drive import drive
from .endpoints.i import antennas, blocking, following, mute, users
from .endpoints.i import i as ep_i
from .endpoints.notes import notes
from .endpoints.reaction import reactions


class Timeline(Enum):
    HOME = "homeTimeline"
    LOCAL = "localTimeline"
    SOCIAL = "hybridTimeline"
    HYBRID = "hybridTimeline"
    GLOBAL = "globalTimeline"


class Bot:
    def __init__(self, address: str, i: Union[str, None]) -> None:
        self.apierrors = []
        self.logger = logging.getLogger("misspy")
        self.address = address
        self._i = i
        self.engine = MiWS_V2
        self.ssl = True
        self.http = AsyncHttpHandler(
            self.address, self._i, self.ssl, logger=self.logger
        )
        self.http_sync = HttpHandler(self.address, self._i, self.ssl)
        self.user: User = User(**self.__i())
        self.funcs: dict = {}
        self.cls = []
        self.endpoint_list = self.endpoints()
        args = {
            "address": self.address,
            "i": self._i,
            "ssl": self.ssl,
            "endpoints": self.endpoint_list,
            "handler": self.http,
        }
        # ---------- endpoints ------------
        self.antennas = antennas(**args)
        self.notes = notes(**args)
        self.drive = drive(**args)
        self.reactions = reactions(**args)
        self.i = ep_i(**args)
        self.blocking = blocking(**args)
        self.mute = mute(**args)
        self.users = users(**args)
        self.following = following(**args)
        # ---------------------------------
        self.reconnectionCoolDown: int = 3

    def __i(self):
        return self.http_sync.send("i", data={})

    def endpoints(self):
        return self.http_sync.send("endpoints", data={})

    def run(self, reconnect=False):
        asyncio.run(self.start())

    async def start(self, reconnect=False):
        self.ws = self.engine(self.address, self._i, self.handler, reconnect, self.ssl)
        await self.handler({"type": "__internal", "body": {"type": "setup_hook"}})
        try:
            await self.ws.start()
        except Exception as e:
            if isinstance(e, self.ws.ConnectionClosedError):
                if reconnect:
                    if isinstance(self.reconnectionCoolDown, int):
                        await asyncio.sleep(self.reconnectionCoolDown)
                    else:
                        await asyncio.sleep(3)
                    await self.start(reconnect)
                else:
                    await self.handler(
                        {
                            "type": "__internal",
                            "body": {
                                "type": "exception",
                                "errorType": e.__class__.__name__,
                                "exc": traceback.format_exc(),
                                "exc_obj": e,
                            },
                        }
                    )
            await self.handler(
                {
                    "type": "__internal",
                    "body": {
                        "type": "exception",
                        "errorType": e.__class__.__name__,
                        "exc": traceback.format_exc(),
                        "exc_obj": e,
                    },
                }
            )

    def event(self, event=""):
        """A decorator that can listen for events in Discord.py-like notation.

        For a list of events, see [documentation](https://docs.misspy.xyz/rewrite/events).

        ## Examples:
        ```python
        @bot.event()
        async def on_ready():
            print("ready!")
        ```

        ↓ Put the event name in the decorator argument.
        ```python
        @bot.event("ready")
        async def ready():
            print("ready!")
        ```

        Args:
            event (str): Name of the event to listen for.
        """

        def decorator(func):
            if event == "":
                ev = func.__name__
            else:
                ev = event
            func.__event_type = ev
            if isinstance(func, staticmethod):
                func = func.__func__
            if not inspect.iscoroutinefunction(func):
                raise TypeError("Functions that listen for events must be coroutines.")
            if self.funcs.get(ev) and isinstance(self.funcs.get(ev), list):
                ev: list = self.funcs.get(ev)
                ev.append(func)
            else:
                self.funcs[ev] = [func]
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

    async def connect(self, channel: Union[str, Timeline], id=None):
        if isinstance(channel, Timeline):
            await self.ws.connect_channel(channel.value, id)
        else:
            await self.ws.connect_channel(channel, id)

    async def handler(self, json: dict):
        try:
            if json["type"] == "channel":
                if json["body"]["type"] == "note":
                    if self.funcs.get("on_note") is None:
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

                    for func in self.funcs["on_note"]:
                        await func(pnote)
                if json["body"]["type"] == "followed":
                    if self.funcs.get("on_followed") is None:
                        return
                    for func in self.funcs["on_followed"]:
                        await func()
        except Exception as e:
            await self.handler(
                {
                    "type": "__internal",
                    "body": {
                        "type": "exception",
                        "errorType": e.__class__.__name__,
                        "exc": traceback.format_exc(),
                        "exc_obj": e,
                    },
                }
            )
        if json["type"] == "__internal":
            if json["body"]["type"] == "setup_hook":
                if self.funcs.get("setup_hook") is None:
                    return
                for func in self.funcs["setup_hook"]:
                    await func()
            if json["body"]["type"] == "ready":
                if self.funcs.get("on_ready") is None:
                    return
                for func in self.funcs["on_ready"]:
                    await func()
            elif json["body"]["type"] == "exception":
                if self.funcs.get("on_error"):
                    eb = {
                        "type": json["body"]["errorType"],
                        "exc": json["body"]["exc"],
                        "exc_obj": json["body"]["exc_obj"],
                    }
                    for func in self.funcs["on_error"]:
                        await func(error(**eb))
                else:
                    if json["body"]["errorType"] in self.apierrors:
                        raise MisskeyAPIError(json["body"]["exc"])
                    else:
                        raise ClientException(json["body"]["exc"])
