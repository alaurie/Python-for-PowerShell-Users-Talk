#! /usr/bin/env python

import argparse
from pathlib import Path

# Parameters
args_parser = argparse.ArgumentParser(
    prog="search-path",
    description="Finds all directories and files in the specified directory",
)

args_parser.add_argument(
    "directory",
    metavar="/search/this/dir",
    type=str,
    help="Enter directory to be searched.",
)

args_parser.add_argument(
    "-p",
    "--print",
    action="store_true",
    help="Print found lists of directories and files",
    required=False,
)

# Lists
directories = []
files = []

# Functions
def search_directory(search_path):
    """Iterates through a directory and adds found files and dirs"""
    all_path_objects = search_path.glob("*")
    for path_object in all_path_objects:
        if path_object.is_dir():
            directories.append(object)
        else:
            files.append(object)


# Main
if __name__ == "__main__":
    args = args_parser.parse_args()
    search_directory(Path(args.directory))
    print(f"We have found {len(directories)} directories and {len(files)} files.")

    if args.print:
        if len(files) != 0:
            print("Here is a list of files found.")
            print(*files, sep="\n")
        else:
            print("No files found to print.")

        if len(directories) != 0:
            print("Here is a list of directories found.")
            print(*directories, sep="\n")
        else:
            print("No directories found to print.")
