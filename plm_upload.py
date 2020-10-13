#!/usr/local/bin/python
from pathlib import Path
import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "paths", metavar="P", type=str, nargs="+", help="paths of files to upload"
)


API_KEY = os.environ.get("STITCH_API_KEY")


def upload_file(file_path: Path):
    """
    Upload a file to a URL
    """
    url = "https://plm-store-api.stitch.fashion/plm/import/"
    files = {"file": (file_path.name, file_path.open("rb"))}
    headers = {
        "x-api-key": API_KEY,
        "x-stitch-client": "plm_uploader",
    }
    response = requests.post(url, files=files, headers=headers)
    response.raise_for_status()
    return response


def main():
    args = parser.parse_args()
    for pathstring in args.paths:
        path = Path(pathstring)
        if not path.exists():
            raise ValueError(f"Path {pathstring} doesnt exist!")
        upload_file(path)
        print(f"Uploaded file {pathstring}!")


if __name__ == "__main__":
    main()
