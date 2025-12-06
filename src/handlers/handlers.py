import math
import networkx as nx
import matplotlib.pyplot as plt
from typing import Any
from src.constants import coordinates, graph_title


def handle_help():
    print(
        "Commands available:"
        "\n  b -- build the graph"
        "\n  i -- get graph analysis"
        "\n  h -- show available commands"
        "\n  q -- quit the program"
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


def handle_info(graph) -> None:
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
