from dataclasses import dataclass
from typing import Optional

"""
Storage device

A storage device stores the binary data.
"""

class Storage:
    
    def __init__(self, path, capacity):
        self.path = path
        self.capacity = capacity

    def create(self):
        """
        This will create the storage file
        """
        
        with open(self.path, "wb") as f:
            data = bytearray([0] * self.capacity)
            f.write(data)

        print(f"Binary file '{self.path}' with {self.capacity} bytes has been created.")

    def write(self, position, content):

        try:
            with open(self.path, "r+b") as f:
                f.seek(position)

                f.write(content)
        
        except FileNotFoundError:
            raise Exception("Storage data not found.")            
        
    def read(self, position, size):

        try:
            with open(self.path, "r+b") as f:
                f.seek(position)

                data = f.read(size)
            
            return data
        
        except FileNotFoundError:
            raise Exception("Storage data not found.")


@dataclass
class Block:
    id: int
    start: int
    empty: bool = True
    next: Optional["Block"] = None