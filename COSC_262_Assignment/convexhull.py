"""
   Convex Hull Assignment: COSC262 (2017)
   Student Name: peizhao,Qiu
   Usercode: pqi13
"""
def lineFn(ptA,ptB,ptC):
    return (
             (ptB[0] - ptA[0]) * (ptC[1] - ptA[1])-
             (ptB[1] - ptA[1]) * (ptC[0] - ptA[0])  )
             
             
def isCCW(ptA,ptB,ptC):
    return (lineFn(ptA, ptB, ptC) > 0)

def theta(pointA,pointB):
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]
    
    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6:
        t = 0
    else:
        t = dy/(abs(dx) + abs(dy))
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
        
    return t * 90
    
        
    

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


def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of 'h' tuples
          [(u0,v0), (u1,v1), ...]    
    """
    
    

    return chull


def grahamscan(listPts):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of 'h' tuples
         [(u0,v0), (u1,v1), ...]  
    """
    #Your implementation goes here
    return  chull


def amethod(listPts):
    """Returns the convex hull vertices computed using 
          a third algorithm
    """
    #Your implementation goes here    
    return chull


def main():
    listPts = readDataPts('Set_A.dat', 2000)  #File name, numPts given as example only
    print(listPts)
    #print(giftwrap(listPts))      #You may replace these three print statements
    #print (grahamscan(listPts))   #with any code for validating your outputs
    #print (amethod(listPts))     

 
if __name__  ==  "__main__":
    main()
  