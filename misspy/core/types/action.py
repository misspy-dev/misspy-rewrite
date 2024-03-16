from typing import Any

import pydantic
from pydantic import dataclasses


@dataclasses.dataclass(config=dict(extra="allow", arbitrary_types_allowed=True))
class APIAction: # anyは一時的。misspy.notes系を読み込むと循環インポートになって動かないからどうにかして解決したい
    reply: Any
    renote: Any