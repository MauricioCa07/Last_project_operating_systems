from queue import Queue

class GenProdCons:
    def __init__(self, size=10):
        self.q = Queue(maxsize=size)
        self.size = size

    def put(self, E):
        self.q.put(E)  

    def get(self):
        return self.q.get() 



    def is_full(self):
        return self.q.qsize() == self.size
    
    def is_empty(self):
        return self.q.empty()
    
    def size(self):
        return self.size
    

    def __len__(self):
        return self.q.qsize()