from functools import wraps
from typing import Callable


def handle_errors(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as error:
            if "is not a valid Command" not in error.__str__():
                print(error)
            return

    return wrapper
