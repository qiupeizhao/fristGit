

def lineFn(ptA,ptB,ptC):
        return (
                (ptB[0] - ptA[0]) * (ptC[1] - ptA[1]) -
                (ptB[1] - ptA[1]) * (ptC[0] - ptA[0]) )

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
 


def min_y_value_point(input_coordinate):
        
        min_index = 0
        
        for index in range(1,len(input_coordinate)):
                
                if input_coordinate[index][1] < input_coordinate[min_index][1]:
                        min_index = index
                elif input_coordinate[index][1] == input_coordinate[min_index][1]:
                        if input_coordinate[index][0] < input_coordinate[min_index][0]:
                                min_index = index                        
        #for index in range(0,len(input_coordinate)):
                #if input_coordinate[index][1] == input_coordinate[min_index][1]:
                        #if input_coordinate[index][0] < input_coordinate[min_index][0]:
                                #min_index = index
        
        return min_index


#in_put = [(1,2),(1,3),(1,10),(1,4),(1,12),(1,-2),(1,-1),(1,0),(1,5)]
#in_put2 = [(-1,1),(2,1),(-2,1),(3,1),(-7,1)]
in_put3 = [(3,3),(-2,3),(2,1),(-2,5),(3,5),(4,1),(-1,1),(1,2),(1,1)]

def add_point(input_list,point,original):
        
        if input_list == []:
                input_list.append(point)
                return input_list
                
        i = 0
        n = len(input_list) 
        
        while i <= n-1 and theta(input_list[i],original) > theta(point, original):
                i = i+1

                
        if  i == n:
                input_list.append(point)                                         
        elif theta(input_list[i],original) < theta(point, original) :
                input_list.insert(i,point)       
        return input_list
                
        
                
                


#print(min_y_value_point(in_put))                       
#def sort_by_angle(original,point_list):
        #point_list = point_list[:]
        #ans_list = []
        #while point_list != []:
                #point = point_list.pop()
                #ans_list = add_point(ans_list, point, original)
        #return ans_list


def sort_by_angle(original,point_list):
        fo = lambda p:theta(original, p)
        ans_list = sorted(point_list[:],key=fo)
        return ans_list

#print(sort_by_angle((0,0), in_put3))
#print(sort_by_angle_1((0,0), in_put3))

def find_special_point(input_coordinate):
        max_x_index = 0
        min_x_index = 0
        max_y_index = 0
        min_y_index = 0
        for index in range(1,len(input_coordinate)):
                
                if input_coordinate[index][0] > input_coordinate[max_x_index][0]: 
                        max_x_index = index
                if input_coordinate[index][0] < input_coordinate[min_x_index][0]: 
                        min_x_index = index     
                if input_coordinate[index][1] > input_coordinate[max_y_index][1]: 
                        max_y_index = index
                if input_coordinate[index][1] < input_coordinate[min_y_index][1]: 
                        min_y_index = index 
                        
                        
        return max_x_index,min_x_index,max_y_index,min_y_index



def generate_input():
        input_list = []
        for i in range(1,6):
                for j in range(1,6):
                        input_list.append((i,j))
                        
        input_list.append((0,2))
        input_list.append((5,0))
        input_list.append((6,4))
        input_list.append((2,6))
        
        #input_list.append((4.5,4.5))
        #input_list.append((4.5,1.5))
        #input_list.append((1.5,1.5))
        #input_list.append((1.5,4.5))        
        return input_list
       
   

def exclude_point(input_list):
        
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

#input_list = generate_input()       
#print(input_list)

#max_x_index,min_x_index,max_y_index,min_y_index =find_special_point(input_list)
#print(input_list[max_x_index],input_list[min_x_index],input_list[max_y_index],input_list[min_y_index])   
#output_list = exclude_point(input_list)
#print(output_list)


#print(isCCW((4, 1), (3, 5),(-2,5)))
#print(sort_by_angle( (0,0) , in_put )) 
#print(sort_by_angle( (0,0) , in_put3 )) 
        
       
        
        


  
    
    

     