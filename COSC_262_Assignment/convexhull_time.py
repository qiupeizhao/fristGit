from test import*
from convexhull import*
from matplotlib import*

import time


def time_test_gift_wrapping(listPts,N):
    
    
    sum_time = 0
    for i in range(N):
        
        copy = listPts[:]
        start = time.clock()
        
        giftwrap(copy)         
        time_period = time.clock() - start
        
        sum_time = time_period + sum_time
    
    return sum_time / N 


def time_test_gham_scan(listPts,N):
    
    sum_time = 0
    for i in range(N):
        
        copy = listPts[:]
        
        start = time.clock()        
        grahamscan(copy)         
        time_period = time.clock() - start
        
        sum_time = time_period + sum_time
    
    return sum_time / N     
    
def time_test_amethod(listPts,N):
    
    sum_time = 0
    for i in range(N):
        
        copy = listPts[:]
        
        start = time.clock()        
        amethod(copy)         
        time_period = time.clock() - start
        
        sum_time = time_period + sum_time
    
    return sum_time / N    
    


def test_1():
    b = []
    a = []
    c = []
    for num in range(2000,32000,2000):

        listPts = readDataPts('Set_B.dat', num)  #File name, numPts given as example only
        t_1 = time_test_gift_wrapping(listPts, 10)
        t_2 = time_test_gham_scan(listPts, 10)
        t_3 = time_test_amethod(listPts,10)
        a.append(t_1)
        b.append(t_2)
        c.append(t_3)
        print(num)
        
    print(a)
    print(b)
    print(c)
    
                        
                        
