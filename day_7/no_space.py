from __future__ import annotations
from dataclasses import dataclass


FS_SZ = 70000000
FREE_REQ = 30000000
MAX_SZ = 100000


@dataclass(frozen=True)
class File:
    "Has name and size"
    name: str
    size: int


class Directory:
    """ Represents a file system directory object. Has parent dir (if not root), subdirs, and files.
    Knows how to return ALL directories and subdirectories.
    Knows how to return total size occupied by this directory and all subdirectories. """

    def __init__(self, name: str) -> None:
        self._name = name
        self._files: list[File] = []  # files in this dir
        self._dirs: list[Directory] = []  # directories in this dir

    @property
    def name(self):
        return self._name

    def add_file(self, a_file: File):
        """ Add a File to this directory """
        self._files.append(a_file)

    def add_directory(self, a_dir: Directory):
        """ Add a Directory to this directory. Set THIS directory to be its parent dir. """
        self._dirs.append(a_dir)
        a_dir.parent_dir = self

    @property
    def parent_dir(self):
        """ Get the parent directory of this dir. """
        return self._parent_dir

    @parent_dir.setter
    def parent_dir(self, a_dir: Directory):
        self._parent_dir = a_dir

    @property
    def directories(self):
        """ Return directories at THIS level. """
        return self._dirs

    def get_directory(self, name: str) -> Directory:
        """ Return a directoy by name, at THIS level. """
        return next(dir for dir in self.directories if dir.name == name)

    def get_all_dirs(self) -> list[Directory]:
        """ Get ALL directories at this level and below. """
        all_dirs = []
        for a_dir in self.directories:
            all_dirs.extend(a_dir.get_all_dirs())

        all_dirs.extend(self.directories)

        return all_dirs

    @property
    def size(self):
        """ The sum of the files in this dir, as well as the sum of all subdirs. """
        return sum(file.size for file in self._files) + sum(dir.size for dir in self._dirs)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, size={self.size}, dirs={len(self.directories)})"


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    root_dir = fs_parse(data)
    print(root_dir)

    # Part 1
    all_dirs = root_dir.get_all_dirs()
    print(f"All dirs count={len(all_dirs)}.")

    # Find all the directories smaller than the target size, and add up their sizes
    small_dirs = [a_dir for a_dir in all_dirs if a_dir.size <= MAX_SZ]
    print(f"\nPart 1: Small dirs total = {sum(dir.size for dir in small_dirs)}")

    # Part 2
    unused_space = FS_SZ - root_dir.size  # Total FS size, minus current used
    extra_free_req = FREE_REQ - unused_space
    print(f"\nCurrent nused space={unused_space}; extra space required={extra_free_req}")

    # Find all directories that would liberate enough space
    # Then we want the smallest that would be big enough.
    dirs_big_enough = [a_dir for a_dir in all_dirs if a_dir.size >= extra_free_req]
    smallest_big_dir = min(dirs_big_enough, key=lambda x: x.size)
    print(f"Part 2: Smallest directory we can delete={smallest_big_dir.name}: {smallest_big_dir.size}")


def fs_parse(instructions: list[str]) -> Directory:
    """ Processes instructions, builds directory tree, and returns the root directory.

    Lines starting with $ are commands
      $ cd ..
      $ cd some_dir
      $ ls

    Else, lines are listings, which show either:
      sz some_file
      dir some_dir
    """
    root_dir = Directory("/")
    current_dir = root_dir

    for line in instructions:
        if line.startswith("$"):  # this line is a command
            cmd_line = line.split()
            cmd = cmd_line[1]
            if cmd == "cd":  # Changing directory
                arg = cmd_line[2]
                if arg == "..":  # Going back up a level
                    current_dir = current_dir.parent_dir
                else:  # Change to named directory
                    if arg == "/":
                        current_dir = root_dir
                    else:
                        # It is possible to have multiple directories with the same name.
                        # But directory names are unique within the current directory.
                        current_dir.get_directory(arg)
        else:  # we must be dir listing
            ls_line = line.split()
            if ls_line[0] == "dir":  # add a new directory
                new_dir = Directory(ls_line[1])
                current_dir.add_directory(new_dir)  # add as subdirectory to current dir
            else:  # must be a file
                file = File(ls_line[1], size=int(ls_line[0]))
                current_dir.add_file(file)

    return root_dir


if __name__ == "__main__":
    main()


