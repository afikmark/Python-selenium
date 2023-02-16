def write(file_path: str, info: str) -> None:
    """
    get file path and the information to write in the file
    writes the file to the input path
    """
    with open(file_path, 'w') as f:
        f.write(info)
