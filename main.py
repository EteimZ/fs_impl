from filesystem import SimpleFS, Storage

storage = Storage(100, "data")
# storage.create()

fs = SimpleFS(storage=storage)

print(fs.blocks[0])
print(fs.block_size)

"""
A file is constitutes of bytes 
"""

# file_content = "hello world"

# fs.create("whatever", file_content)
# # # print(fs.root_dir)

# file_obj = fs.open("whatever")
# print(file_obj)

# content = fs.read(file_obj)

# print(content)


# fs.write(file_obj, "Happy new year!")

# for block in fs.blocks:
#      print(block.start)

# content = fs.read(file_obj)

# print(content)

# fs.append(file_obj, " 2024")

# content = fs.read(file_obj)

# print(content)
# file_obj.get_metadata()

# fs.info()

fs.delete("whatever")
