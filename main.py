from filesystem import SimpleFS, Storage

storage = Storage("store.bin", 10)
storage.create()

fs = SimpleFS(storage=storage)

print(fs.blocks[0])
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

# for block in fs.blocks:
#     print(block.data)

print(file_obj.read())

file_obj.append(" 2024")

print(file_obj.read())
file_obj.get_metadata()

fs.info()