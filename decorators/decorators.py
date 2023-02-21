from utils.logger import logger
import logging
from typing import Callable, Any, Optional
from functools import wraps, partial


def with_logging(func: Callable[..., Any], log: Optional[logging.Logger] = None) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        logger = log or logging.getLogger(__name__)
        logger.info(f"Calling {func.__name__}")
        value = func(*args, **kwargs)
        logger.info(f"Finished calling {func.__name__}")
        return value

    return wrapper


logger = logger
default_logging = partial(with_logging, log=logger)


def retry(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any):
        success = func(*args, **kwargs)
        tries = 0
        while not success and tries < 3:
            logger.warning(f"Retrying {func.__name__}")
            if not success:
                success = func(*args, **kwargs)
                tries += 1

    return wrapper
