from pydantic import dataclasses

@dataclasses.dataclass(config=dict(extra="allow"))
class mspy:
    tlId: str

@dataclasses.dataclass(config=dict(extra="allow"))
class error:
    type: str
    exc: str
    exc_obj: Exception