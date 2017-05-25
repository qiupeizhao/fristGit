from test import*
from convexhull import*
from matplotlib import*

import time


def time_test_gift_wrapping(listPts,N):
    """
    THis function return the average runing time for
    Gift-Wrapping algorithm over N time for input coordinate

    """   
    sum_time = 0
    
    for i in range(N):
        
        copy = listPts[:] # make a copy of the input list
        
        start = time.clock()    # start the timer 
        chull = giftwrap(copy)  # runing the algorithm        
        time_period = time.clock() - start  # caculate the runing time for the Gift-wrapping algorithm  
        
        sum_time = time_period + sum_time  # summing the time for different runing cases
    
    return sum_time / N # return the average runing time for the algorithm


def time_test_gham_scan(listPts,N):
    
    """
    THis function return the average runing time for
    grahamscan algorithm over N time for input coordinate

    """   
    sum_time = 0
    
    for i in range(N):
        
        copy = listPts[:] # make a copy of the input list
        
        start = time.clock()    # start the timer 
        chull = grahamscan(copy)   # runing the algorithm        
        time_period = time.clock() - start  # caculate the runing time for the Gift-wrapping algorithm  
        
        sum_time = time_period + sum_time  # summing the time for different runing cases
    
    return sum_time / N # return the average runing time for the algorithm    
    
     
                
    
    
def time_test_amethod(listPts,N):
    
    """
    THis function return the average runing time for
    the third algorithm over N time for input coordinate

    """   
    sum_time = 0
    
    for i in range(N):
        
        copy = listPts[:] # make a copy of the input list
        
        start = time.clock()    # start the timer 
        chull = amethod(copy)      # runing the algorithm
        time_period = time.clock() - start  # caculate the runing time for the Gift-wrapping algorithm  
        
        sum_time = time_period + sum_time  # summing the time for different runing cases
    
    return sum_time / N # return the average runing time for the algorithm 
    


def time_test():
    b = []
    a = []
    c = []
    
    # run the test through different number of test point
    for num in range(2000,32000,2000):

        listPts = readDataPts('Set_B.dat', num)  #File name, numPts given as example only
        t_1 = time_test_gift_wrapping(listPts, 5)
        t_2 = time_test_gham_scan(listPts, 5)
        t_3 = time_test_amethod(listPts,1)
        a.append(t_1)
        b.append(t_2)
        c.append(t_3) 
        print(num)
        
    print(a)
    print(b)
    print(c)
    
time_test()


        
        
    
 

                       
