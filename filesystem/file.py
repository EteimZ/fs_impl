from dataclasses import dataclass
from datetime import datetime
from .block import Block


@dataclass
class MetaData:
    file_size: float
    created: datetime
    last_modified: datetime
    last_accessed: datetime


@dataclass
class File:
    name: str
    start_block: Block
    meta_data: MetaData

    def get_metadata(self):
        print(f"File size: {self.meta_data.file_size} bytes")
        print(f"Last accessed: {self.meta_data.last_accessed}")
        print(f"Last modified: {self.meta_data.last_modified}")
        print(f"Created: {self.meta_data.created}")
