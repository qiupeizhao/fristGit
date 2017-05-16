"""
   Convex Hull Assignment: COSC262 (2017)
   Student Name: peizhao,Qiu
   Usercode: pqi13
"""
from test import*    
    
#def isCCW(ptA,ptB,ptC):
    #return (lineFn(ptA, ptB, ptC) > 0)

#def theta(pointA,pointB):
    #dx = pointB[0] - pointA[0]
    #dy = pointB[1] - pointA[1]
    
    #if abs(dx) < 1.e-6 and abs(dy) < 1.e-6:
        #t = 0
    #else:
        #t = dy/(abs(dx) + abs(dy))
    #if dx < 0:
        #t = 2 - t
    #elif dy < 0:
        #t = 4 + t
        
    #return t * 90
    
        
    

def readDataPts(filename, N):
    """Reads the first N lines of data from the input file
          and returns a list of N tuples
          [(x0,y0), (x1, y1), ...]
    """
    i = 0
    listPts = []
    for line in open(filename, 'r'):
        if i < N:
            coordinate = line.rstrip() 
            (x,y) = coordinate.split()
            listPts.append((float(x),float(y)))
            i = i + 1    
    
    return listPts

def min_y_value_point(input_coordinate):

    min_index = 0

    for index in range(1,len(input_coordinate)):
        if input_coordinate[index][1] < input_coordinate[min_index][1]:
            min_index = index

    for index in range(0,len(input_coordinate)):
        if input_coordinate[index][1] == input_coordinate[min_index][1]:
            if input_coordinate[index][0] < input_coordinate[min_index][0]:
                min_index = index
                #select right most

    return min_index

def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of 'h' tuples
          [(u0,v0), (u1,v1), ...]    
    """
    pts = listPts[:]
    i = 0
    v = 0
    start_point_index = min_y_value_point(listPts)
    pts.append(listPts[start_point_index])    
    k = start_point_index
    n = len(pts) 
    while k != n-1:
        pts[i],pts[k] = pts[k],pts[i]
        minAngle = 361
        for j in range(i,n):
            angle = theta(pts[i], pts[j])
            if (angle < minAngle and angle > v and pts[j] != pts[i]):
                minAngle = angle;
                k = j   #do we need to 
        i = i + 1
        v = minAngle
    
    chull = pts[:i]
    
    return chull


def grahamscan(listPts):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of 'h' tuples
         [(u0,v0), (u1,v1), ...]  
    """
    copy = listPts[:]
    start_point_index = min_y_value_point(listPts)
    start_point = copy .pop(start_point_index)
    chull = [start_point]
    order_list = sort_by_angle(start_point,copy)
    
    chull.append(order_list.pop())
    chull.append(order_list.pop())
    
    while order_list != []:
        
        point_next = order_list.pop()
        while isCCW(chull[-2], chull[-1],point_next) is False:
            chull.pop()  
        if isCCW(chull[-2], chull[-1],point_next) is True:
            chull.append(point_next)
    
    return  chull


def amethod(listPts):
    """Returns the convex hull vertices computed using 
          a third algorithm
    """
    #Your implementation goes here    
    return chull


def main():
    print()
    listPts = readDataPts('Set_A.dat', 500)  #File name, numPts given as example only
    print(listPts)
    print(giftwrap(listPts))      #You may replace these three print statements
    print(len(giftwrap(listPts)))
    print (grahamscan(listPts))   #with any code for validating your outputs
    #print (amethod(listPts))   
    

 
if __name__  ==  "__main__":
    main()
  