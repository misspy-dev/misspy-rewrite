from typing import Union

from pydantic import dataclasses

from .note import Pin

@dataclasses.dataclass()
class mute:
    id: str
    createdAt: str
    expiresAt: Union[str, None]
    muteeId: str
    mutee: Pin