from collections import deque

class GenProdCons:
    def __init__(self, size=10):
        self.q = deque(maxlen=size)
        self.size = size

    def put(self, E):
        self.q.append(E)  

    def get(self):
        while True:
            if not len(self.q) ==  0:
                return self.q.popleft() 
            break


    def is_full(self):
        return len(self.q) == self.size
    
    def is_empty(self):
        return len(self.q) ==  0
    
    def size(self):
        return self.size