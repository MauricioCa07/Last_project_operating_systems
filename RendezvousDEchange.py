from threading import Thread

class RendezvousDEchange:
    def __init__(self):
        self.numbers =  [None] * 2  
        self.flag = True


    def echanger(self,E):
        if self.numbers[0] == None:
            self.numbers[0] = E
            while self.flag:
                pass
            return self.numbers[1]
        else:
            self.numbers[1] = E
            self.flag = False
            return self.numbers[0]

        
        

        
