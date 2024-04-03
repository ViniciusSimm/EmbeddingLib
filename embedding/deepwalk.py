import random
import matplotlib.pyplot as plt
import networkx as nx
from word2vec import Word2Vec

class DeepWalk():
    def __init__(self, graph):
        self.graph = graph

    def random_walk(self, walk_length):
        # Inicia a caminhada em um nó aleatório
        start_node = random.choice(list(self.graph.nodes()))
        walk = [start_node]
        while len(walk) < walk_length:
            cur_node = walk[-1]
            neighbors = list(self.graph.neighbors(cur_node))
            if not neighbors:
                break
            next_node = random.choice(neighbors)
            walk.append(next_node)
        return walk

    def generate_random_walks(self, num_walks=10, walk_length=80):
        walks = []
        for _ in range(num_walks):
            walk = self.random_walk(walk_length)
            walks.append(walk)
        return walks