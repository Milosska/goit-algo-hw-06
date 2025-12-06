from src.constants import Command
from src.helpers import parse_input, initialize_graph
from src.handlers import (
    handle_help,
    handle_graph_build,
    handle_info,
    handle_compare_bfs_and_dfs,
)


def main():
    print("Hello!")
    obuchiv_graph = initialize_graph()

    handle_help()

    while True:
        command = parse_input(input("Please, enter the command: "))

        match command:
            case Command.QUIT:
                print("Goodbye!")
                break

            case Command.HELP:
                handle_help()

            case Command.BUILD:
                handle_graph_build(obuchiv_graph)

            case Command.INFO:
                handle_info(obuchiv_graph)

            case Command.COMPARE:
                handle_compare_bfs_and_dfs(obuchiv_graph)

            case _:
                print("Invalid command. Please, use one of the listed below.")


if __name__ == "__main__":
    main()
