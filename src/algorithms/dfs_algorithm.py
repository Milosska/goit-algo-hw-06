import networkx as nx


def dfs_algorithm(
    graph: nx.Graph, vertex="Обухів", vertex_sequence=[], stack=None
) -> list[str]:
    vertex_sequence.append(vertex)
    neighbors = list(graph.neighbors(vertex))

    for neighbor in neighbors:
        if neighbor not in vertex_sequence:
            dfs_algorithm(graph, neighbor, vertex_sequence, stack)

    return vertex_sequence
