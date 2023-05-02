
from pathlib import Path
import sys


def get_dirs_and_files(p="."):
    root = Path(p)

    directories = []
    files = []

    for i in root.iterdir():
        if i.is_dir():
            directories.append(i)
        else:
            files.append(i)

    return directories, files


if __name__ == "__main__":
    args = sys.argv[1:]

    if args:
        p = args[0]

        dirs, files = get_dirs_and_files(p)

        print("Directories:")
        print(dirs)
        print()

        print("Files:")
        print(files)
    else:
        print("Please provide a path on the computer!")
