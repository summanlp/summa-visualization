
from graph import PygraphWrapper as pygraph

def get_graph(sequence):
    graph = pygraph()
    for item in sequence:
        if not graph.has_node(item):
            graph.add_node(item)
    return graph


def remove_unreacheable_nodes(graph):
    for node in graph.nodes():
        if sum(graph.edge_weight((node, other)) for other in graph.neighbors(node)) == 0:
            graph.del_node(node)
