
 


def min_y_value_point(input_coordinate):
        
        min_index = 0
        
        for index in range(1,len(input_coordinate)):
                if input_coordinate[index][1] < input_coordinate[min_index][1]:
                        min_index = index
                        
        for index in range(0,len(input_coordinate)):
                if input_coordinate[index][1] == input_coordinate[min_index][1]:
                        if input_coordinate[index][0] < input_coordinate[min_index][0]:
                                min_index = index
        
        return min_index


in_put = [(1,2),(5,3),(7,2),(9,10),(3,4),(4,2)]
print(min_y_value_point(in_put))                       
        

       
  
    
    

     