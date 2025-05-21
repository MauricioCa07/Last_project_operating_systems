#using this beacuse the teacher used this and it manages the order
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
        return self.q.full()
    
    def is_empty(self):
        return self.q.empty()
    
    def size(self):
        return self.size
    
    #We override the len() method bc the teacher 
    #was using it. I dont want to change the tests
    def __len__(self):
        return self.q.qsize()