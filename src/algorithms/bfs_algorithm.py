import networkx as nx
from queue import Queue


def bfs_algorithm(graph: nx.Graph, start_vertex="Обухів") -> list[str]:
    vertex_sequence = []
    vertex_sequence.append(start_vertex)

    queue: Queue = Queue()
    queue.put(start_vertex)

    while not queue.empty():
        current_vertex = queue.get()
        neighbors = list(graph.neighbors(current_vertex))

        for neighbor in neighbors:
            if neighbor not in vertex_sequence:
                vertex_sequence.append(neighbor)
                queue.put(neighbor)

    return vertex_sequence
