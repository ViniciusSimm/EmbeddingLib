import numpy as np
from scipy.sparse import csgraph
from scipy.sparse.linalg import eigsh

class LaplacianEigenmaps:
    def __init__(self, graph):
        self.graph = graph
        self.model = None
        self.embedding = None

    def create_model(self, vector_size=100):
        # Construct the normalized Laplacian matrix
        self.model = csgraph.laplacian(self.graph, normed=True)
        self.vector_size = vector_size + 1  # plus one to exclude the zero eigenvalue eigenvector

    def train(self):
        if not self.model:
            raise Exception("Model not created. Call create_model() before train().")

        # Compute the eigenvalues and eigenvectors
        eigenvalues, eigenvectors = eigsh(self.model, k=self.vector_size, which='SM')

        # Exclude the first eigenvector to get the desired dimensionality
        self.embedding = eigenvectors[:, 1:]