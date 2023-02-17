import json


def write(file_path: str, info: str) -> None:
    """
    get file path and the information to write in the file
    writes the file to the input path
    """
    with open(file_path, 'w') as f:
        f.write(info)


def read_from_json(file_path: str) -> dict:
    with open(file_path, 'r') as json_file:
        json_reader = json.load(json_file)
    return json_reader
