from pathlib import Path
from sys import argv
from shutil import copy, rmtree

if __name__ == "__main__":
    dirName = "."
    if len(argv) > 1:
        dirName = argv[1]
    files = list(filter(lambda file: file.stat().st_size < 2048 and not file.is_dir(), Path(dirName).glob("*")))
    if len(files) == 0:
        print(f"No files < 2Kb in {dirName}")
    else:
        newDirPath = Path("small")
        if newDirPath.exists():
            rmtree(newDirPath)
        newDirPath.mkdir(exist_ok=True)
        print(f"All files < 2Kb in {dirName}:")
        for file in files:
            print(file.name, end=' ')
            copy(file, newDirPath)
        print()
    