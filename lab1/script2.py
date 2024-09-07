from argparse import ArgumentParser
from pathlib import Path

def outDirectoryInfo(path):
    directoryFiles = list(filter(lambda file: not file.is_dir(), path.glob("*")))
    print(f"{path} directory info:")
    print(f"Number of files: {len(directoryFiles)}")
    print(f"Sum of file sizes: {sum([file.stat().st_size for file in directoryFiles])}Kb")


def outListOfFiles(outFile, listOfFiles):
    for file in listOfFiles:
        outFile.write(f"{file}\n")
        print(file)


def outFiles(path, files, outInDirectoryFile="out_dir.txt", outNotInDirectoryFile="out_not_dir.txt"):
    directoryFiles = list(map(lambda file: file.name, filter(lambda file: not file.is_dir(), path.glob("*"))))
    filesInDirectory = [file for file in files if file in directoryFiles]
    filesNotInDirectory = [file for file in files if file not in directoryFiles]
    with open(outInDirectoryFile, "w") as outFile:
        print(f"Files in directory {path}:")
        outListOfFiles(outFile, filesInDirectory)
    with open(outNotInDirectoryFile, "w") as outFile:
        print(f"Files not in directory {path}:")
        outListOfFiles(outFile, filesNotInDirectory)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--dirpath", default=".")
    parser.add_argument("--files", nargs="+")
    path = Path(parser.parse_args().dirpath)
    files = parser.parse_args().files
    if (files is None):
        print("No file specified.")
        outDirectoryInfo(path)
    else:
        print(f"{len(files)} files specified.")
        outFiles(path, files)        
