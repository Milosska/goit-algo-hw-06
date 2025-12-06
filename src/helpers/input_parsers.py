from src.decorators.decorators import handle_errors
from src.constants import Command


@handle_errors
def parse_input(user_input: str) -> Command:
    if user_input is None:
        raise ValueError("Invalid command. Please, use one of the listed below.")

    command = Command(user_input)
    return command
