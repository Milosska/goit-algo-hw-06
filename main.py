from src.constants import Command
from src.helpers import parse_input


def main():
    print("Hello!")

    while True:
        command = parse_input(
            input(
                "Please, select the mode to continue:"
                '\n-- for getting the graph of Obuchiv region (task 1) print "1"'
                '\n-- for exiting the program print "q"'
                "\n"
            )
        )

        match command:
            case Command.QUIT:
                print("Goodbye!")
                break

            case Command.TASK_ONE:
                print("Task one implementation.")

            case _:
                print("Invalid command. Please, use one of the listed below.")


if __name__ == "__main__":
    main()
