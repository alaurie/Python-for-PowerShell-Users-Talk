#!/usr/bin/env python

import pycdlib
import argparse
import requests
from pathlib import Path

arg_parser = argparse.ArgumentParser(
    prog="extract-wimfile", description="Extract install.wim from Windows 10 ISO."
)

arg_parser.add_argument(
    "iso",
    metavar="file.iso",
    type=str,
    help="Enter the filepath of the ISO to extract wim file from.",
)

arg_parser.add_argument(
    "output_path",
    metavar="/output/path",
    type=str,
    help="Enter the output path for the wim file.",
)

arg_parser.add_argument(
    "filename",
    metavar="filename.wim",
    type=str,
    help="Enter filename for extracted wim file.",
)

args = arg_parser.parse_args()


def extract_wim(iso, target_path):
    iso_file = Path(iso)
    target_path = Path(target_path)
    output = Path.joinpath(target_path, "install.wim")
    iso = pycdlib.PyCdlib()
    iso.open(iso_file)
    iso.get_file_from_iso(output, udf_path="/sources/install.wim")
    iso.close()


if __name__ == "__main__":
    extract_wim(args.iso, args.output_path)
