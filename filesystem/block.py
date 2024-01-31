from dataclasses import dataclass
from typing import Optional
import json
import os

"""
Storage device

A storage device stores the binary data.
"""


class Storage:
    def __init__(self, capacity, path="data"):
        self.path = path
        self.capacity = capacity
        self.directory = {}
        self.binary_file = os.path.join(self.path, "store.bin")
        self.data_file = os.path.join(self.path, "data.json")

        # Check if the directory already exists
        if not os.path.exists(self.path):
            # If not, create the directory
            os.makedirs(self.path)
            print(f"Directory '{self.path}' created successfully.")
        else:
            print(f"Directory '{self.path}' already exists.")

    def create(self):
        """
        This will create the storage file
        """
        # Specify the file name and path within the directory

        with open(self.binary_file, "wb") as f:
            data = bytearray([0] * self.capacity)
            f.write(data)

        print(
            f"Binary file '{self.binary_file}' with {self.capacity} bytes has been created."
        )

        # Write the empty JSON data to the file
        with open(self.data_file, "w") as f:
            json.dump({"root_dir": "/", "files": {}}, f)

        print(f"Data file: '{self.binary_file}' has been created.")

    def write(self, position, content):

        try:
            with open(self.binary_file, "r+b") as f:
                f.seek(position)

                f.write(content)

        except FileNotFoundError:
            raise Exception("Storage data not found.")

    def read(self, position, size):

        try:
            with open(self.binary_file, "r+b") as f:
                f.seek(position)

                data = f.read(size)

            return data

        except FileNotFoundError:
            raise Exception("Storage data not found.")

    def create_block(self, json_block):
        if json_block is None:
            return None

        return Block(
            id=json_block["id"],
            start=json_block["start"],
            empty=json_block["empty"],
            next=self.create_block(json_block["next"]),
        )

    def get_data(self):

        with open(self.data_file, "r") as f:
            data = json.load(f)

        return data

    def write_data(self, file_name, new_data):
        with open(self.data_file, "r+") as f:
            data = self.get_data()
            data["files"][file_name] = new_data
            json.dump(data, f)
    
    def delete_data(self, file_name):
        data = self.get_data()

        with open(self.data_file, "w") as f:
            data["files"].pop(file_name)
            json.dump(data, f)


@dataclass
class Block:
    id: int
    start: int
    empty: bool = True
    next: Optional["Block"] = None
