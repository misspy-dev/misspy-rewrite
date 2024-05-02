
from typing import Union, List, Any

from pydantic import dataclasses
from mitypes import UserLite

@dataclasses.dataclass()
class RequestList:
    id: str
    follower: UserLite
    followee: UserLite