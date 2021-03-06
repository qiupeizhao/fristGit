"""
   Convex Hull Assignment: COSC262 (2017)
   Student Name: peizhao,Qiu
   Usercode: pqi13
"""
from test import*    

 

def readDataPts(filename, N):
    """Reads the first N lines of data from the input file
          and returns a list of N tuples
          [(x0,y0), (x1, y1), ...]
    """
    # Open the input file: 
    fo = open(filename, 'r')
    
    # Initilize answear list:
    listPts = []
    
    # Extract N coordinate from input file
    for i in  range(N):
        
        # Read a single coordinate
        coordinate = fo.readline() 
        
        # Format the coordinate into tuple and add to output list
        (x,y) = coordinate.split()
        listPts.append((float(x),float(y)))    
    
    return listPts


def giftwrap(copy):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of 'h' tuples
          [(u0,v0), (u1,v1), ...]    
    """
    
    # initial the list index and the local minimum angle 
    i = 0
    v = 0
    
    # find the start point which is the right most minimum y value 
    
    # find the index of the right most button point
    start_point_index = min_y_value_point(copy)
    
    # append the start point into the operation point
    # as end point for operating list
    copy.append(copy[start_point_index])  
    
    # k represent the point to at i location
    # in the first iteration (i = 0) , the 
    # next point to be sweep is minimum y value
    # point
    k = start_point_index
    
    # find the length of the array 
    n = len(copy) 
    
    # iterate when next point is not start point
    while k != n-1:
    
        # sweep the position of current point to ...
        # point have the smallest angle between horizental line
        copy[i],copy[k] = copy[k],copy[i]
        
        # going throught the remian unvisited point ....
        # to find the point with the smallest angle ....
        # from horizental point (have to be bigger than ...
        # the previous smallest angle to avoid turning special 
        # case)
        minAngle = 361
        
        for j in range(i,n):
            angle = theta(copy[i], copy[j])
            
            # deal with the case when return to starting point 
            if abs(angle) < 1.e-6:
                angle = 360
                
            # going through the remaining point in the list to find the smallest angle point 
            if (angle < minAngle and angle > v and copy[j] != copy[i]):
                minAngle = angle;
                k = j  
                
        # move to find the next point 
        i = i + 1
        
        # record the current smallest point, the next smallest most bigger than it 
        v = minAngle
    
    # return the ans_list at i index from operating list since it is when...
    # the complete the convex hull and return to starting point
    chull = copy[:i]  
    return chull


def grahamscan(copy):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of 'h' tuples
         [(u0,v0), (u1,v1), ...]  
    """

   
    # find the start point which is the right most minimum y value 
       
    start_point_index = min_y_value_point(copy)
    
    # append the start point into the operation stock
    start_point = copy.pop(start_point_index)
    chull = [start_point]
    
    # sort the input the list according to the angle which they....
    # make with the starting point

    order_list = sort_by_angle(start_point,copy)   
    
    # append the first element in the sorted list.... 
    # since it must in the convex hull
    chull.append(order_list.pop(0))
    chull.append(order_list.pop(0))
    
    # iterate through the list
    for point in order_list:
        
        # if the last two point don't make a anti-clock-wise turn with.... 
        # the current point in sorted list dump the last point in the....
        # operating list
        while isCCW(chull[-2], chull[-1],point) is False :
            chull.pop()
            
        # if it does make a anti-clock_wise turn with
        # the current point in the sorted list ....
        # add the current point to the operating list
        if isCCW(chull[-2], chull[-1],point) is True:
            chull.append(point)
            
    # after iterating through the point in the sorted list return 
    # the ans list
    return  chull


def amethod(listPts):
    """Returns the convex hull vertices computed using 
          a modified Gift-Wrapping algorithm 
    """
    # pre-processing step which exclude points inclose by 
    # the trangular made by the extremal point
    
    pre_list = exclude_point(listPts)
    
    # Run the Gift-Wrapping Algorithm over the pre-proccessed input set 
    chull = giftwrap(pre_list)
    return chull


def main():
    
    listPts = readDataPts('Set_B.dat', 1000)  #File name, numPts given as example only
    
    copy_1 = listPts[:]     # make a copy of input list
    copy_2 = listPts[:]     # make a copy of input list
    copy_3 = listPts[:]     # make a copy of input list
    copy_4 = listPts[:]     # make a copy of input list
    
    print(giftwrap(copy_4))      # runing the Gift-wrapping algrithm over input-list
 
    print (grahamscan(copy_2))   #runing the Graham-Scan algorithm over input-list
    
    print (amethod(copy_3))   #runing the improved version of Gift-wrapping algorithm over input-list
    

 
if __name__  ==  "__main__":
    main()
  
  