# File System Implementation

A visual file system implemented in Python built for educational purposes.

A file system serves as the interface between an operating system and the storage device. Its role is to establish a logical representation of the storage device. Without the file system, you would have to manually write to the storage device.

Various operating systems have different file system implementations. The goal of this project is to understand how file systems are implemented. The entire implementation is done in software.

## Usage

To use this program, all you need is Python 3.8 and higher. No external dependencies are required.

```bash
git clone https://github.com/EteimZ/fs_impl
cd fs_impl
python main.py
```

## Explanation

The repository currently has three major classes:
- **SimpleFS**
- **Block**
- **File**

**SimpleFS** is the file system implementation. It contains a [single-level directory](https://www.codingninjas.com/studio/library/structures-of-directory). This implementation uses [non-contiguous memory allocation](https://www.youtube.com/watch?v=B1_er2nGKao&list=PLWCT05ePsnGww5psXWHRLG7p30eKKt1Pd&index=21), which is implemented using a [linked list](https://en.wikipedia.org/wiki/Linked_list). The node of the linked list is the **Block**. A block contains a fixed size of data. A collection of linked blocks forms a **File**. **SimpleFS** can contain as many files as possible, provided they don't exceed its capacity.


## Example

Let's create a simple file system:

```python
from filesystem import SimpleFS

fs = SimpleFS()
```

By default a simple file system has a capicity of 10. This means it can have only 10 blocks. With block size of 5. This means each block size can have only 5 bytes.


Let's create a file:

```python
file_content = "hello world"

fs.create("whatever.txt", file_content)
```

The `fs.create` method is used to create a file.

```python
file_obj = fs.open("whatever.txt")
```

The `fs.open` method is used to create a file object which is an Instance of **File**.

We can read from it:

```python
content = file_obj.read()
```

We can write to it as well:

```python
file_obj.write("Writing to the file.")
```

The Block class is not directly accessible.

## Resources

- [File system explanation](https://www.youtube.com/watch?v=_h30HBYxtws) by [ExplainingComputers](https://www.youtube.com/@ExplainingComputers)
- [Files and File Systems](https://www.youtube.com/results?search_query=file+system+udacity+playlist) by [Crash Course](https://www.youtube.com/@crashcourse)
- [File Allocation Table](https://www.youtube.com/watch?v=V2Gxqv3bJCk) explanation by udacity. 