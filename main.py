import threading
from prod_cons import GenProdCons
import random
import time


library = GenProdCons()

def producer():
    while True:
        if not library.is_full():
            n = random.random()
            if n <= 0.33:
                library.put(1)
                print(f"El elemento producido fue un {1}\n")
            if 0.33 > n <= 0.66:
                library.put(2)
                print(f"El elemento producido fue un {2}\n")
            if n > 0.66:
                library.put(3)
                print(f"El elemento producido fue un {3}\n")
        
def consumer():
    while True :
        if not library.is_empty():
            print(f"El objeto consumido fue: {library.get()}")

def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()



if __name__=="__main__":
    main()






