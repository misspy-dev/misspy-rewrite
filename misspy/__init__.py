from importlib.metadata import version 

from .Bot import Bot
from .settings import Option, extension

from .core.types import *
from .core.experimental import aiows
from .core import websocket

__version__ = version("misspy")

MSC = aiows.MSC # Misskey
MIWS_V2 = websocket.MiWS_V2