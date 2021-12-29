import os


def _secret_dir():
    path = os.path.join(os.path.expanduser('~'), '__pikz__')
    os.makedirs(path, exist_ok=True)
    return path