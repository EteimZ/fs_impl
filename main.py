"""
Implement a simple filesystem in python

The filesystem will consists of blocks. It uses a linkedlist to connect each block to form 
file. The directory structure used is a single level directory. 
"""

from filesystem import SimpleFS


fs = SimpleFS()
print(fs.blocks[0])
print(fs.capacity)
print(fs.block_size)

"""
A file is constitutes of bytes 
"""

file_content = "hello world"

fs.create("whatever", file_content)
print(fs.root_dir)

file_obj = fs.open("whatever")
print(file_obj)

file_obj.read()
print(file_obj.filesystem)

file_obj.write("Happy new year!")

for block in fs.blocks:
    print(block.data)

print(file_obj.read())

file_obj.append(" 2024")

print(file_obj.read())
file_obj.get_metadata()

fs.info()