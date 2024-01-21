"""
Implement a simple filesystem in python

The filesystem will consists of blocks. It uses a linkedlist to connect each block to form 
file. The directory structure used is a single level directory. 
"""

from dataclasses import dataclass, field
from typing import Dict, Optional, List
from datetime import datetime
from dataclasses import asdict
import json
import random

from .block import Block, Storage
from .file import File, MetaData


@dataclass
class SimpleFS:
    """
    This filesystem will have a file allocation table.
    The blocks determine how many
    """

    storage: Storage
    block_size: int = 5
    blocks: List[Block] = field(default_factory=list)
    root_dir: Dict[str, File] = field(default_factory=dict)

    def __post_init__(self):
        with open("data.json", "r") as f:
            self.root_dir = json.load(f)

        for i in range(self.storage.capacity):
            self.blocks.append(Block(id=i, start=i * 5))

    def open(self, file_name) -> Optional[File]:
        """
        This will give the user access to an existing file.
        """

        file = self._get_file(file_name)

        if file:
            file.meta_data.last_accessed = datetime.now().isoformat()
            return file
        else:
            raise Exception("File doesn't exist.")

    def read(self, file: File):
        """
        There will be a function to read it's content
        """

        def traverse_blocks(block: Block):
            if block.next == None:
                return self.storage.read(block.start, self.block_size)
            else:
                return self.storage.read(
                    block.start, self.block_size
                ) + traverse_blocks(block.next)

        return traverse_blocks(file.start_block)

    def write(self, file: File, content):
        """
        This will write to a currently existing file.
        """

        self.unlink(file.name)
        file_blocks = self.create_blocks(content)

        file.start_block = file_blocks[0]
        file.meta_data.last_modified = datetime.now().isoformat()

    def append(self, file: File, new_content):
        """
        This will create new blocks and apend it to the last block in the file
        """

        new_blocks = self.create_blocks(new_content)

        def append_to_end(block: Block, new_block: Block):
            if block.next == None:
                block.next = new_block
                return

            append_to_end(block.next, new_block)

        file.meta_data.last_modified = datetime.now().isoformat()
        append_to_end(file.start_block, new_blocks[0])

    def create_blocks(self, content):
        encoded_bytes = bytearray(content, "utf-8")

        if len(encoded_bytes) > self.free_space:
            raise Exception("Space not available")

        chunks = [
            encoded_bytes[i : i + self.block_size]
            for i in range(0, len(encoded_bytes), self.block_size)
        ]
        num_chunks = len(chunks)
        n = 1
        file_blocks: List[Block] = []

        while n <= num_chunks:
            block = random.choice(self.blocks)

            if block.empty:
                block.next = None
                block.empty = False
                self.storage.write(block.start, chunks[n - 1])
                file_blocks.append(block)
                n += 1

        def connect_blocks(lst: List[Block]):
            if len(lst) != 1:
                lst[0].next = lst[1]
                connect_blocks(lst[1:])

        connect_blocks(file_blocks)

        return file_blocks

    def create(self, file_name, content):
        """
        This will create a new file.
        """

        file = self._get_file(file_name)

        if file:
            raise Exception("File already exists.")

        file_blocks = self.create_blocks(content)

        size = sum(
            [
                len(self.storage.read(block.start, self.block_size))
                for block in file_blocks
            ]
        )

        meta_data = MetaData(
            file_size=size,
            created=datetime.now().isoformat(),
            last_accessed=datetime.now().isoformat(),
            last_modified=datetime.now().isoformat(),
        )

        self.root_dir[file_name] = File(
            name=file_name,
            start_block=file_blocks[0],
            meta_data=meta_data,
        )

        with open("data.json", "r+") as f:
            data = asdict(self.root_dir[file_name])
            json.dump(data, f)
        
        print("File created successfully.")

    def ls(self):
        """
        This list everything in the root directory
        """

        for i, key in enumerate(self.root_dir.keys(), start=1):
            print(key, end="  ")
            if i % 2 == 0:
                print()

        print()

    def tree(self):
        """
        This is used to show tree representation of the directory.
        """
        print("/")
        for file in self.root_dir.keys():
            print(f" - {file}")

    def delete(self, filename):
        self.unlink(filename)

        del self.root_dir[filename]

        print("File deleted successfully.")

    def unlink(self, filename):
        """
        This will delete a file.
        """

        file = self._get_file(filename)

        if not file:
            raise Exception("File doesn't exist.")

        def mark_empty(block: Block):
            if block.next == None:
                block.empty = True
                return

            else:
                block.empty = True
                return mark_empty(block.next)

        mark_empty(file.start_block)

    def _get_file(self, filename: str) -> Optional[File]:
        """
        This function tries to get the file from the directory.
        Returns a file if it suceeds, returns None if it fails.
        """

        file = self.root_dir.get(filename, None)
        return file

    @property
    def total_space(self):
        return self.storage.capacity * self.block_size

    @property
    def free_space(self):
        free_blocks = [block for block in self.blocks if block.empty]
        return len(free_blocks) * self.block_size

    def info(self):
        print(f"Total space: {self.total_space} bytes")
        print(f"Free space: {self.free_space} bytes")
