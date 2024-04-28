from pydantic import dataclasses

from .note import Note

@dataclasses.dataclass()
class favorite:
    id: str
    createdAt: str
    note: Note
    noteId: str