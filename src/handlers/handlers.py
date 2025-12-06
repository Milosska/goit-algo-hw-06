import math
import networkx as nx
import matplotlib.pyplot as plt
from typing import Any
from src.constants import coordinates, graph_title
from src.algorithms import bfs_algorithm, dfs_algorithm, dijkstra_algorithm


def handle_help():
    print(
        "Доступні команди:"
        "\n  b -- побудувати граф"
        "\n  i -- отримати аналітику по графу"
        "\n  c -- порівняти DFS та BFS алгоритми"
        "\n  h -- показати доступні команди"
        "\n  q -- вихід з програми"
        "\n"
    )


def handle_graph_build(graph: nx.Graph) -> None:
    # Set main params
    pos = coordinates
    node_weights = [data["weight"] for _, data in graph.nodes(data=True)]
    node_sizes = list(
        map(lambda weight: (max(node_weights) - weight + 1) * 100, node_weights)
    )
    node_colors = [
        data["color"] if "color" in data else "#2f670b"
        for _, data in graph.nodes(data=True)
    ]

    nx.draw(graph, pos, with_labels=False, node_size=node_sizes, node_color=node_colors)

    # Move node labels below the nodes
    label_pos: dict[Any, tuple[float, float]] = {
        node: (float(x), float(y) - 0.0175) for node, (x, y) in pos.items()
    }
    nx.draw_networkx_labels(graph, label_pos, font_size=7)

    # Indicate edges weight
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels={
            (u, v): f"{data['weight']} км" for u, v, data in graph.edges(data=True)
        },
        font_size=5,
    )

    plt.title(graph_title)
    plt.show()


def handle_info(graph: nx.Graph) -> None:
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    is_connected = nx.is_connected(graph)
    density = nx.density(graph)
    clustering = nx.average_clustering(graph)
    avg_degree = sum(dict(graph.degree()).values()) / graph.number_of_nodes()
    avg_centrality = (
        sum(dict(nx.degree_centrality(graph)).values()) / graph.number_of_nodes()
    )

    print(
        f"\nПобудовано граф '{graph_title}'.\n"
        f"Основні показники графу:\n"
        f"{' ' * 4}Кількість вершин: {num_nodes}\n"
        f"{' ' * 4}Кількість ребер: {num_edges}\n"
        f"{' ' * 4}Зв'язність: {'Так' if is_connected else 'Ні'}\n"
        f"{' ' * 4}Щільність графу: {math.ceil(density * 10000) / 10000}\n"
        f"{' ' * 4}Середній ступінь вершин: {math.ceil(avg_degree * 10000) / 10000}\n"
        f"{' ' * 4}Середній коефіцієнт кластеризації: {math.ceil(clustering * 10000) / 10000}\n"
        f"{' ' * 4}Середній коефіцієнт центральності: {math.ceil(avg_centrality * 10000) / 10000}\n"
    )


def handle_compare_bfs_and_dfs(graph: nx.Graph):
    print(f"Починаємо порівняння DFS та BFS алгоритмів для графу '{graph_title}'.")

    print("Запускаємо BFS алгоритм...")
    bfs_visit_sequence = bfs_algorithm(graph)
    print(
        f"\nПослідовність вершин для BFS алгоритму: {' --> '.join(bfs_visit_sequence)}\n"
    )

    print("Запускаємо DFS алгоритм...")
    dfs_visit_sequence = dfs_algorithm(graph)
    print(
        f"\nПослідовність вершин для DFS алгоритму: {' --> '.join(dfs_visit_sequence)}\n"
    )

    print("Порівняння завершено.")


def handle_dijkstra(graph: nx.Graph):
    print(f"Запускаємо алгоритм Дейкстри для графу '{graph_title}'.")
    node_min_distances = dijkstra_algorithm(graph)

    print("Найменші відстані від населеного пункту Обухів:")
    for node, node_info in node_min_distances.items():
        print(
            f"{' ' * 4}{node}: {' --> '.join(node_info.path)}. Протяжність маршруту {node_info.distance} км"
        )

    print("Розрахунок відстаней завершено.")
