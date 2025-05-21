class RendezvousDEnchange:
    def __init__(self):
        self.numbers =  [None] * 2  

    def echager(self,E):
        if self.numbers[0] != None and self.numbers[1] != None: 
            temp = self.numbers[0]
            self.numbers[0] = self.numbers[1]
            self.numbers[1] = temp
        if self.numbers[0] == None: self.numbers[0] = E
        elif self.numbers[1] == None: self.numbers[1] = E

        

        
