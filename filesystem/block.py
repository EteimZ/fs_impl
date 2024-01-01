from dataclasses import dataclass
from typing import Optional


@dataclass
class Block:
    id: int
    data: bytearray
    empty: bool = True
    next: Optional["Block"] = None
