from src.constants import Command
from src.helpers import parse_input, initialize_graph
from src.handlers import (
    handle_help,
    handle_graph_build,
    handle_info,
    handle_compare_bfs_and_dfs,
    handle_dijkstra,
)


def main():
    print("Привіт!")
    obuchiv_graph = initialize_graph()

    handle_help()

    while True:
        command = parse_input(input("Будь-ласка, введіть команду: "))

        match command:
            case Command.QUIT:
                print("До побачення!")
                break

            case Command.HELP:
                handle_help()

            case Command.BUILD:
                handle_graph_build(obuchiv_graph)

            case Command.INFO:
                handle_info(obuchiv_graph)

            case Command.COMPARE:
                handle_compare_bfs_and_dfs(obuchiv_graph)

            case Command.DIJKSTRA:
                handle_dijkstra(obuchiv_graph)

            case _:
                print(
                    "Некоректна команда. Будь-ласка введіть валідну команду або натисніть 'h' для виводу списку команд."
                )


if __name__ == "__main__":
    main()
