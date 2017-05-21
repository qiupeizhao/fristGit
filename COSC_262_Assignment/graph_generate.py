from test import*
from convexhull import*
from matplotlib import*
from convexhull_time import*
import matplotlib.pyplot as plot
from matplotlib import pyplot


def plot_data_set():
    plot.figure()
    listPts = readDataPts('Set_B.dat', 30)  #File name, numPts given as example only

    x = []
    y = []
    for (x_value,y_value) in  listPts:
        x.append(x_value)
        y.append(y_value)
        
    plot.scatter(x,y,label = 'data',color='r',s = 5)
    plot.xlabel('x axis') 
    plot.ylabel('y axis')
    plot.grid()
    plot.title('Data_Set_A with 3000 input')
    
    
    plot.figure()
    listPts = readDataPts('Set_A.dat', 30)  #File name, numPts given as example only  
    copy = listPts[:]
    
    convex_hull = grahamscan(copy)
    x = []
    y = []
    
    

    
    for (x_value,y_value) in  listPts:
        x.append(x_value)
        y.append(y_value)
        
    for i in range(len(convex_hull)-1):
    
        drawline(convex_hull[i],convex_hull[i+1] )
        
    drawline(convex_hull[0],convex_hull[-1] )
    
    plot.scatter(x,y,label = 'data',color='b',s = 5)
    plot.xlabel('x axis') 
    plot.ylabel('y axis')
    plot.grid()
    plot.title('Data_Set_B with 3000 input')
    plot.show()

    
    
    
def plot_data_set_1():
    plot.figure()
    listPts = readDataPts('Set_B.dat', 600)  #File name, numPts given as example only  
    copy = listPts[:]
    max_x_index,min_x_index,max_y_index,min_y_index =find_special_point(copy)
    drawline(copy[min_y_index], copy[max_x_index],'k')
    drawline(copy[max_x_index], copy[max_y_index],'k')
    drawline(copy[max_y_index], copy[min_x_index],'k')
    drawline(copy[min_x_index], copy[min_y_index],'k')    
    convex_hull = grahamscan(copy)
    x = []
    y = []
    for (x_value,y_value) in  listPts:
        x.append(x_value)
        y.append(y_value)
        
    #for i in range(len(convex_hull)-1):
    
        #drawline(convex_hull[i],convex_hull[i+1] )
        
    #drawline(convex_hull[0],convex_hull[-1] )
    
    plot.scatter(x,y,label = 'data',color='b',s = 5)
    plot.xlabel('x axis') 
    plot.ylabel('y axis')
    plot.grid()
    plot.title('Data_Set_B with 600 input')
    plot.show()    
    
    
    
    
    
def test():
    b = []
    a = []
    c = []
    N_list = []
    for num in range(2000,32000,2000):
        N_list.append(num)
        listPts = readDataPts('Set_A.dat', num)  #File name, numPts given as example only
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
    plot.plot(N_list,a)
    plot.plot(N_list,b)
    plot.plot(N_list,c)
    plot.title('Time take with increase data point')
    plot.xlabel('number of input point') 
    plot.ylabel('Time taking (Sec)') 
    plot.legend(['Gift wrapping','Graham_Scan','A_method'])
    plot.grid()
    plot.show()


#plot_data_set()



def drawline(point_1,point_2, color = 'r'):
    plot.plot([point_1[0],point_2[0]],[point_1[1],point_2[1]],color= color)
    #plot.show()



test()