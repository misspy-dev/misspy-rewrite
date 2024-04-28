from pydantic import dataclasses

from .note import Pin


@dataclasses.dataclass()
class blocking_list:
    id: str
    createdAt: str
    blockeeId: str
    blockee: Pin
