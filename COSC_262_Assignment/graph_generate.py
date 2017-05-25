from test import*
from convexhull import*
from matplotlib import*
from convexhull_time import*
import matplotlib.pyplot as plot
from matplotlib import pyplot


def plot_data_set():
    """
    THis function plot the data set A and data set B 
    """    
    plot.figure()
    listPts = readDataPts('Set_A.dat', 3000)  #File name, numPts given as example only

    x = []
    y = []
    
    for (x_value,y_value) in  listPts:
        x.append(x_value)
        y.append(y_value)
        
    plot.scatter(x,y,label = 'data',color='r',s = 0.5)
    plot.xlabel('x axis',fontsize = 16) 
    plot.ylabel('y axis',fontsize = 16)
    plot.grid()
    plot.title('Data_Set_A with 3000 input')
   
    
    plot.figure()
    listPts = readDataPts('Set_B.dat', 3000)  #File name, numPts given as example only  
      
    x = []
    y = []

    for (x_value,y_value) in  listPts:
        x.append(x_value)
        y.append(y_value)
        
    
    plot.scatter(x,y,label = 'data',color='b',s = 0.5)
    plot.xlabel('x axis',fontsize = 16) 
    plot.ylabel('y axis',fontsize = 16)
    plot.grid()
    plot.title('Data_Set_B with 3000 input')
    plot.show()

    
    
    
def plot_convex_hull():
    plot.figure()
    listPts = readDataPts('Set_B.dat', 600)  #File name, numPts given as example only  
    copy = listPts[:]
    max_x_index,min_x_index,max_y_index,min_y_index =find_special_point(copy)
    out = exclude_point(copy)
    drawline(copy[min_y_index], copy[max_x_index],'k')
    drawline(copy[max_x_index], copy[max_y_index],'k')
    drawline(copy[max_y_index], copy[min_x_index],'k')
    drawline(copy[min_x_index], copy[min_y_index],'k')    
    convex_hull = grahamscan(copy)
    
    x = []
    y = []
    for (x_value,y_value) in  copy:
        x.append(x_value)
        y.append(y_value)    
    
    plot.scatter(x,y,label = 'data',color='r',s = 5)
    
    x = []
    y = []
    for (x_value,y_value) in  out:
        x.append(x_value)
        y.append(y_value)
        
    for i in range(len(convex_hull)-1):
    
        drawline(convex_hull[i],convex_hull[i+1] )
        
    drawline(convex_hull[0],convex_hull[-1] )
    
    plot.scatter(x,y,label = 'data',color='b',s = 5)
    plot.xlabel('x axis',fontsize = 12) 
    plot.ylabel('y axis',fontsize = 12)
    plot.grid()
    plot.title('Data_Set_B with 600 input',fontsize = 13)
    plot.show()    
    
    
    
    
    
def camparison_plot():
    """
    THis function plot the time take for different algorithm over data set A and data set B
    for comparison
    """        
    b = []
    a = []
    c = []
    N_list = []
    for num in range(2000,32000,2000):
        N_list.append(num)
        listPts = readDataPts('Set_A.dat', num)  #File name, numPts given as example only
        t_1 = time_test_gift_wrapping(listPts, 5)
        t_2 = time_test_gham_scan(listPts, 5)
        t_3 = time_test_amethod(listPts,5)
        a.append(t_1)
        b.append(t_2)
        c.append(t_3)
        print(num)
        
    print(a)
    print(b)
    print(c)
    plot.plot(N_list,a,color = 'b')
    plot.plot(N_list,b,color = 'r')
    plot.plot(N_list,c)
    plot.title('Time Complexity for three Alternative methods',fontsize = 13)
    plot.xlabel('Number of input point',fontsize = 12) 
    plot.ylabel('Time taking (Sec)',fontsize = 12) 
    plot.legend(['Gift wrapping','Graham_Scan','A_method'])
    plot.grid()
    plot.show()





def drawline(point_1,point_2, color = 'r'):
    """
    THis function draw the line between different data point
    """     
    plot.plot([point_1[0],point_2[0]],[point_1[1],point_2[1]],color= color)
   
    
def N_H():
    """
    THis function draw the graph shows the ration between the number of point in the
    convex hull and the number of point between different data point
    """         
    a = []
    b = []
    N_list = []    
    for num in range(2000,32000,2000): 
        N_list.append(num)    
        listPts_1 = readDataPts('Set_A.dat', num)
        listPts_2 = readDataPts('Set_B.dat', num)
        a.append(len(grahamscan(listPts_1)))         
        b.append(len(grahamscan(listPts_2)))
        
        
    print(a)
    print(b)
    

    plot.plot(N_list,a,color = 'b')
    plot.plot(N_list,b,color = 'r')
   
    plot.title('Number of input point vs convex vertices',fontsize = 13)
    plot.xlabel('Number of input point',fontsize = 12) 
    plot.ylabel('Number of convex verties',fontsize = 12) 
    plot.legend(['Set_A','Set_B'])
    plot.grid()
    plot.show()
    
    

    


plot_convex_hull()