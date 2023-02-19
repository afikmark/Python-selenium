
from typing import Callable, Any


def retry(func: Callable[..., Any]) -> Callable:
    def wrapper(*args: Any):
        success = func(*args)
        tries = 0
        while not success and tries < 3:
            if not success:
                success = func(*args)
                tries += 1

    return wrapper
