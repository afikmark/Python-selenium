def write(file_path: str, info):
    with open(file_path, 'w') as f:
        f.write(info)
