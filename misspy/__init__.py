from importlib.metadata import version 

from .Bot import Bot # noqa: F401
from .settings import Option, extension  # noqa: F401

from .core.types import *  # noqa: F403
from .core.experimental import aiows
from .core import websocket

__version__ = version("misspy")

MSC = aiows.MSC # Misskey
MIWS_V2 = websocket.MiWS_V2

homeTimeline = "homeTimeline"
localTimeline = "localTimeline"
socialTimeline = "hybridTimeline"
hybridTimeline = "hybridTimeline"
globalTimeline = "globalTimeline"

class visibility:
    public = "public"
    home = "home"
    followers = "followers"
    specified = "specified"