import networkx as nx
from src.decorators.decorators import handle_errors
from src.constants import Command


@handle_errors
def parse_input(user_input: str) -> Command:
    if user_input is None:
        raise ValueError("Invalid command. Please, use one of the listed below.")

    command = Command(user_input.lower().strip())
    return command


def initialize_graph() -> nx.Graph:
    graph: nx.Graph = nx.Graph()
    graph.add_nodes_from(
        [
            ("Обухів", {"weight": 1, "color": "#dd4b4b"}),
            ("Таценки", {"weight": 2, "color": "#2b6fad"}),
            ("Козин", {"weight": 2, "color": "#2b6fad"}),
            ("Нові Безрадичі", {"weight": 3}),
            ("Романків", {"weight": 3}),
            ("Підгірці", {"weight": 3}),
            ("Старі Безрадичі", {"weight": 3}),
            ("Копачів", {"weight": 3}),
            ("Григорівка", {"weight": 3}),
            ("Гусачівка", {"weight": 3}),
            ("Матяшівка", {"weight": 3}),
            ("Слобідка", {"weight": 3}),
            ("Красне Перше", {"weight": 3}),
            ("Долина", {"weight": 3}),
            ("Дерев'яна", {"weight": 3}),
            ("Трипілля", {"weight": 2, "color": "#2b6fad"}),
            ("Халеп'я", {"weight": 3}),
            ("Витачів", {"weight": 3}),
            ("Стайки", {"weight": 3}),
            ("Українка", {"weight": 2, "color": "#2b6fad"}),
            ("Плюти", {"weight": 3}),
        ]
    )

    graph.add_weighted_edges_from(
        [
            ("Обухів", "Таценки", 7.8),
            ("Таценки", "Козин", 8.6),
            ("Обухів", "Нові Безрадичі", 12.2),
            ("Нові Безрадичі", "Таценки", 11.4),
            ("Нові Безрадичі", "Романків", 11.7),
            ("Романків", "Підгірці", 2.7),
            ("Обухів", "Старі Безрадичі", 12.3),
            ("Старі Безрадичі", "Копачів", 22.0),
            ("Обухів", "Григорівка", 8.1),
            ("Григорівка", "Гусачівка", 3.0),
            ("Григорівка", "Матяшівка", 3.9),
            ("Гусачівка", "Матяшівка", 5.1),
            ("Матяшівка", "Слобідка", 4.5),
            ("Обухів", "Красне Перше", 6.5),
            ("Красне Перше", "Долина", 4.4),
            ("Дерев'яна", "Трипілля", 7.8),
            ("Обухів", "Дерев'яна", 6.8),
            ("Трипілля", "Халеп'я", 4.1),
            ("Халеп'я", "Витачів", 6.4),
            ("Халеп'я", "Стайки", 7.5),
            ("Обухів", "Українка", 9.9),
            ("Українка", "Трипілля", 7.8),
            ("Українка", "Плюти", 6.0),
        ]
    )

    return graph
