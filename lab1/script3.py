from pathlib import Path
from sys import argv


if __name__ == "__main__":
    dirPath = "."
    if len(argv) > 1:
        dirPath = argv[1]
    path = Path(dirPath)
    if not path.exists():
        path.mkdir(exist_ok=True)
    with open("out_not_dir.txt") as inFile:
        files = inFile.read().split("\n")[:-1]
        [Path(f"{dirPath}/{file}").write_text('') for file in files]
