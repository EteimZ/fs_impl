from dataclasses import dataclass
from datetime import datetime
from .block import Block

# Added to prevent circular imports
try:
    from .simple import SimpleFS
except ImportError:
    pass


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
    filesystem: "SimpleFS"

    def read(self):
        """
        There will be a function to read it's content
        """

        def traverse_blocks(block: Block):
            if block.next == None:
                return self.filesystem.storage.read(block.start, self.filesystem.block_size) 
            else:
                return self.filesystem.storage.read(block.start, self.filesystem.block_size) + traverse_blocks(block.next)

        return traverse_blocks(self.start_block)

    def write(self, content):
        """
        This will write to a currently existing file.
        """

        fs = self.filesystem

        fs.unlink(self.name)
        file_blocks = fs.create_blocks(content)

        file = fs._get_file(self.name)

        file.start_block = file_blocks[0]
        file.meta_data.last_modified = datetime.now()

    def append(self, new_content):
        """
        This will create new blocks and apend it to the last block in the file
        """

        fs = self.filesystem

        new_blocks = fs.create_blocks(new_content)

        def append_to_end(block: Block, new_block: Block):
            if block.next == None:
                block.next = new_block
                return

            append_to_end(block.next, new_block)

        file = fs._get_file(self.name)

        file.meta_data.last_modified = datetime.now()
        append_to_end(self.start_block, new_blocks[0])

    def get_metadata(self):
        print(f"File size: {self.meta_data.file_size} bytes")
        print(f"Last accessed: {self.meta_data.last_accessed}")
        print(f"Last modified: {self.meta_data.last_modified}")
        print(f"Created: {self.meta_data.created}")
