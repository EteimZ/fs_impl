# File System Implementation

A virtual file system implemented in Python built for educational purposes.

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

The repository currently has four major classes:
- **SimpleFS**
- **Storage**
- **Block**
- **File**

**SimpleFS** is the file system implementation. It contains a [single-level directory](https://www.codingninjas.com/studio/library/structures-of-directory). This implementation uses [non-contiguous memory allocation](https://www.youtube.com/watch?v=B1_er2nGKao&list=PLWCT05ePsnGww5psXWHRLG7p30eKKt1Pd&index=21), which is implemented using a [linked list](https://en.wikipedia.org/wiki/Linked_list). It communicates with the **Storage** which is a virtual representation of a storage device(Hard disk or Flash drive). When the **SimpleFs** class is created it creates blocks. Which are a group of **Block**. These blocks map to the storage device. A **File** is a group of related blocks.



## Example

First we import our required classes:

```python
from filesystem import SimpleFS, Storage
```

Then we create our storage device:

```python
storage = Storage("store.bin", 10)
storage.create()
```

The **Storage** class is creating a file called `store.bin`. Which will be used to persist the memory.
We are also creating it with a size of 10.

Now let's create a our file system and asign our created `storage` to it:

```python
fs = SimpleFS(storage=storage)
```

By default a simple file system sets it block size to 5. This means each block size can have only 5 bytes.


Let's create a file:

```python
file_content = "hello world"

fs.create("whatever.txt", file_content)
```

The `fs.create` method is used to create a file.

```python
file_obj = fs.open("whatever.txt")
```

The `fs.open` method is used to get access to a file object which is an Instance of **File**.

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