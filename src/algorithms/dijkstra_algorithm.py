import networkx as nx
from dataclasses import dataclass
from typing import List


@dataclass
class NodeInfo:
    distance: float
    path: List[str]


def dijkstra_algorithm(graph: nx.Graph, start_vertex="Обухів"):
    node_distances: dict[str, NodeInfo] = {
        vertex: NodeInfo(float("inf"), []) for vertex in graph
    }
    node_distances[start_vertex] = NodeInfo(0.0, [])

    nodes_to_visit = list(graph.nodes())

    while nodes_to_visit:
        # Find the vertex with current min distance in the node_distances
        current_vertex = min(
            nodes_to_visit, key=lambda vertex: node_distances[vertex].distance
        )

        current_info = node_distances[current_vertex]
        current_min_distance = current_info.distance
        current_info.path.append(current_vertex)

        # If the min value of vertex is infinity, there's no path to it, so we break the cycle
        if current_min_distance == float("inf"):
            break

        neighbors = list(graph.neighbors(current_vertex))
        for neighbor in neighbors:
            neighbor_info = node_distances[neighbor]
            weight = graph[current_vertex][neighbor]["weight"]
            neighbor_min_distance = current_min_distance + weight

            if neighbor_info.distance > neighbor_min_distance:
                neighbor_info.distance = neighbor_min_distance
                neighbor_info.path = [path for path in current_info.path]

        nodes_to_visit.remove(current_vertex)

    return node_distances
