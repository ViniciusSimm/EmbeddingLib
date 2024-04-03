from sknetwork.embedding import SVD as SVD_embedding

class SVD():
    def __init__(self, graph):
        self.graph = graph
    
    def create_model(self, vector_size=100):
        self.model = SVD_embedding(vector_size)

    def train(self, data):
        if not self.model:
            raise Exception("Model not created. Call create_model() before train().")
        
        self.embedding = self.model.fit_transform(data)

