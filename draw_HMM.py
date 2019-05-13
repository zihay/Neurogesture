import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Tuple
Frequency = List[Tuple[any, int]]


def draw(state: Frequency, transition: Frequency):
    plt.figure(figsize=(8, 8))
    G = nx.Graph()
    node = [s[0] for s in state]
    node = [str(v) for v in node]
    node_size = [s[1] for s in state]
    nx.draw(G, node_size=node_size)
    plt.show()
