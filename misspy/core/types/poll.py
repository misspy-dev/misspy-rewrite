from typing import List, Union

from pydantic import dataclasses

@dataclasses.dataclass
class Poll:
    choices: List[str]
    multiple: bool = False
    expiresAt: Union[int, None]
    expiredAfter: Union[int, None]