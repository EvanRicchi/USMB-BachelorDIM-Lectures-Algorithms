# -*- coding: utf-8 -*-
##
#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : a set of generic functions for data management

def average_above_zero(input_list):
    ##
    # Basic function able to return the average of the positive elements of a list
    # @param input_list: the input list to be scanned

    # Init critical variable
    positive_values_sum=0
    positive_values_count=0
    
    # Compute the average of positive elements of a list
    for item in input_list:
        # Select only positive items
        if item>0:
            positive_values_sum+=item
            positive_values_count+=1
        elif item==0:
            print('This value is null:'+str(item))
        else:
            print('This value is negative:'+str(item))
    # Compute the final average
    average=float(positive_values_sum)/float(positive_values_count)
    print('Positive elements average is '+str(average))
    return float(average)

# Testing average above zero function :
mylist=[1,2,3,4,-7]
result=average_above_zero(mylist)
message='The average of positive samples of {list_values} is {res}'.format(list_values=mylist,res=result)
print(message)

def max_value(input_list):
    ##
    # Basic function able to return the max value of a list
    # @param input_list: the input list to be scanned
    # @throws an exception (ValueError) on an empty list
    
    # First check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    # Init max value
    max_val=input_list[0]
    max_idx=0
    # Compute the max value elements of a list
    """
    for item in input_list:
        # Select only positive items
        if max_val<item:
            max_val=item
    return max_val
    """
    for idx, item in enumerate(input_list):
        # Select only positive items
        if max_val<item:
            max_val=item
            max_idx=idx
    return max_val, max_idx

# Testing max value function :
mylist2=[-1,2,-20]
mymax, mymaxidx=max_value(mylist2)
message='Max value of {input_list} is {max_scan} with the position {idx}'.format(input_list=mylist2,max_scan=mymax,idx=mymaxidx)
print(message)

def reverse_table(input_list):
    ##
    # Basic function able to reverse a list
    # @param input_list: the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    # First check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    
    lastIdx=len(input_list)
    # Compute a list reversed
    for idx in range(len(input_list)/2):
        lastIdx-=1
        popped=input_list[idx]
        input_list[idx]=input_list[lastIdx]
        input_list[lastIdx]=popped
        return input_list
        
    # Compute a list reversed using python slice notation
    """
    reversed_list=input_list[::-1]
    return reversed_list
    """
    
# Testing reverse table function :
mylist3=[-1,2,-20]
reversed_list=reverse_table(mylist3)
message='The reversed list is {after_reverse}'.format(after_reverse=reversed_list)
print(message)


# Matrix processing lib
import numpy as np

# Set a value in a specific cell
"""
myMat[1,3]=1
"""

# Filling something in the matrix
"""
for row in range(5,8):
        for col in range(7,9):
            myMat[row,col]=1
print(myMat)
"""
# Filling something in the matrix (a nice way)
"""
myMat[2:4,5:9]=1
myMat[2:4,5:9]=np.ones([2,4])
print(myMat)
"""
# Output coordinates matrix
"""
bbox_coords=np.zeros([4,2], dtype=int)
"""
def roi_bbox(input_image):
    ##
    # Function able to compute the bounding box coordinates of an object
    # @param input_image: the input image to be scanned
    
    # Initialise variables 
    # [xmin,ymin;xmax,ymin]
    # [xmin,ymax;xmax,ymax]
    #
    size_rows=10
    size_cols=10
    xmin=size_cols
    xmax=0
    ymin=size_rows
    ymax=0
    
    # Compute coordinates of the bounding box 
    for row in range(0,size_rows):
        for cols in range(0,size_cols):
            if input_image[row,cols]>0:
                if xmin>row:
                    xmin=row
                if xmax<row:
                    xmax=row
                if ymin>cols:
                    ymin=cols
                if ymax<cols:
                    ymax=cols
    
    bounding_box_coordinates = np.array([[ymin,xmin],[ymax,xmin],[ymin,ymax],[ymax,xmax]])
    return bounding_box_coordinates

# Initialise matrice and testing bbox function
size_rows=10
size_cols=10
myMat=np.zeros([size_rows, size_cols], dtype=int)
myMat[2:4,5:9]=np.ones([2,4])
coordinates_bbox=roi_bbox(myMat)
print(coordinates_bbox)
print(myMat)

def random_fill_sparse(input_array, vfill):
    ##
    # Function able to fill K cells with value X while the others
    # should remain empty with a 2D array of shape N X N whose cell type is char
    # @param input_array: the input array to be scanned
    # @param vfill: a random number

    # Initialise variables
    table_size = len(input_array)
    i = 0
    
    #Fill the table until the counter is equal to zero
    for rows in range(0,table_size):
        for cols in range(0,table_size):
            if i < vfill:
                input_array[rows,cols]='X'
                i+=1
    
    # @return: return the array fill with the value X                          
    return input_array             

# Importation of the function randint from the library random
from random import randint

def random(vfill):
    ##
    # Function able to return a random number
    # @param input_array: the input array to be scanned
    # @param vfill: a random number

    random = randint(0,vfill)

    # @return: return a random number
    return random



# Initialise input array and testing random_fill_sparse function

input_array=np.chararray((10, 10))
input_array[:] = ''

vfill= input_array.size
random = alea(vfill)

result = random_fill_sparse(input_array,random)
print(result)

def remove_whitespace(input_string):
    ##
    # Function able to parse a string and remove all its whitespace
    # without the use of any other table
    # @param input_string: the input string to be scanned

    # Initialise variable
    string = ""
     
    # Find whitespaces and put characters expect whitespaces in a variable called string
    for i in input_string:
        if i != " ":
            string += i

    # @return: return the string without whitespaces
    return string; 
 

# Testing remove_whitespace function
test = "This is a sentence with whitespaces"
result = remove_whitespace(test)
print(result)        






