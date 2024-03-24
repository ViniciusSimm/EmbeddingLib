class Word2Vec():

    def __init__(self):
        pass

    def create_model(self, vector_size=100, window=5, min_count=1, workers=4):
        from gensim.models import Word2Vec

        self.model = Word2Vec(vector_size=vector_size,
                        window=window,
                        min_count=min_count,
                        workers=workers)
        
    def train(self, data, epochs = 10):
        self.model.build_vocab(data)
        self.model.train(data, total_examples=self.model.corpus_count, epochs=epochs)
    
    def get_vector(self,string):
        return self.model.wv.get_vector(string)
    
    def get_similar_vectors(self, vector, num_vectors=5):
        return self.model.wv.similar_by_vector(vector, topn=num_vectors)