import matplotlib.pyplot as plt
import networkx as nx

class Graph():
    def __init__(self):
        self.graph = None

    def create_graph(self,data):
        G = nx.Graph()
        for path in data:
            nx.add_path(G, path)
        
        self.graph = G

    def draw_graph(self):

        nx.draw(self.graph, with_labels=True)
        plt.show()

    def get_nodes(self):
        if self.graph is not None:
            self.nodes = list(self.graph.nodes())
        else:
            return []
    
    def generate_adjacency_matrix(self):
        if self.graph is None:
            raise ValueError("Graph is not created. Call create_graph first.")
        
        self.adjacency_matrix = nx.adjacency_matrix(self.graph).toarray()