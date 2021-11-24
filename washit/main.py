#!/usr/bin/python3

from program import Program
from washer import Washer
from datetime import datetime as dt
from datetime import timedelta



def main():
    washers = []
    number_of_washers = 12
    for _ in range(number_of_washers):
        washers.append(Washer())
        
    for w in washers:
        pass
        #print(w)
        
    w1 = Washer()
    w2 = Washer()
    
    w1.book(dt.now(), 'kokvask')
    print(w1)
   
    w2.book(dt.now(), 'kokvask')
    print(w2)


if __name__ == "__main__":
    main()
