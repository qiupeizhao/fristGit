

def lineFn(ptA,ptB,ptC):
        return (
                (ptB[0] - ptA[0]) * (ptC[1] - ptA[1]) -
                (ptB[1] - ptA[1]) * (ptC[0] - ptA[0]) )

def isCCW(ptA,ptB,ptC):        
        '''this function return whether the point AB form a anti-clock rotation 
        with point C'''
        return (lineFn(ptA, ptB, ptC) > 0)



def theta(pointA,pointB):        
        '''This function return the angle formed by line
        AB and horizental line '''
        
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
 


def min_y_value_point(input_coordinate):
        '''This function return the point have the smallest y_value in the 
            input list'''        
        min_index = 0       
        for index in range(1,len(input_coordinate)):
                
                if input_coordinate[index][1] < input_coordinate[min_index][1]:
                        min_index = index
                elif input_coordinate[index][1] == input_coordinate[min_index][1]:
                        if input_coordinate[index][0] < input_coordinate[min_index][0]:
                                min_index = index                        
        
        return min_index




def sort_by_angle(original,point_list):
        '''this function return the sorted list base on 
        the angle they made with horizental line'''
        
        fo = lambda p:theta(original, p)
        ans_list = sorted(point_list[:],key=fo)
        return ans_list


def find_special_point(input_coordinate):
        '''this function return the four extral point from 
        input point '''
              
        max_x_index = 0
        min_x_index = 0
        max_y_index = 0
        min_y_index = 0
        
        for index in range(len(input_coordinate)):
                
                if input_coordinate[index][0] > input_coordinate[max_x_index][0]: 
                        max_x_index = index
                if input_coordinate[index][0] < input_coordinate[min_x_index][0]: 
                        min_x_index = index     
                if input_coordinate[index][1] > input_coordinate[max_y_index][1]: 
                        max_y_index = index
                if input_coordinate[index][1] < input_coordinate[min_y_index][1]: 
                        min_y_index = index 
                        
                        
        return max_x_index,min_x_index,max_y_index,min_y_index




       
   

def exclude_point(input_list):
        '''this function return the points which not inclose by the quadrilateral formed 
            four extral point'''        
        
        max_x_index,min_x_index,max_y_index,min_y_index =find_special_point(input_list)
        max_x = input_list[max_x_index]
        min_x = input_list[min_x_index]
        max_y = input_list[max_y_index]
        min_y = input_list[min_y_index]
        output_list = []
        for point in input_list:
               
                if isCCW(min_y, max_x, point) == False:
                        output_list.append(point)
                elif isCCW(max_x, max_y, point) == False:
                        output_list.append(point)
                elif isCCW(max_y, min_x, point) == False:
                        output_list.append(point)
                elif isCCW(min_x, min_y, point) == False:
                        output_list.append(point)
        return output_list               

        
       
        
        


  
    
    

     