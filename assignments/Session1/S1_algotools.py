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
    
    # @return: return the average of the positive elements of the list
    return float(average)

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
    for idx, item in enumerate(input_list):
        # Select only positive items
        if max_val<item:
            max_val=item
            max_idx=idx
            
    # @return: return the max value of a list
    return max_val

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
    
    for idx in range(int(len(input_list)/2)):
        lastIdx-=1
        popped=input_list[idx]
        input_list[idx]=input_list[lastIdx]
        input_list[lastIdx]=popped
        
    # @return: return the reversed list
    return input_list
    
    """   
    # Compute a list reversed using python slice notation
    reversed_list=input_list[::-1]
    return reversed_list
    """
    
# Matrix processing lib
import numpy as np

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
    # @return: return the coordinates of the bounding box
    return bounding_box_coordinates

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

def remove_whitespace(input_string):
    ##
    # Function able to parse a string and remove all its whitespace
    # without the use of any other table
    # @param input_string: the input string to be scanned
    
    # First check if provided string is not empty
    if len(input_string)==0:
        raise ValueError('provided string is empty')
        
    # Initialise variable
    string = ""
     
    # Find whitespaces and put characters expect whitespaces in a variable called string
    for i in input_string:
        if i != " ":
            string += i

    # @return: return the string without whitespaces
    return string; 

import random as rd
def shuffle(input_list):
    ##
    # Function able to efficiently randomly select items of a list
    # @param input_list: the input list to be scanned
    
    # First check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
        
    # Initialise variables
    list_size=len(input_list)

    # Compute the shuffle
    input_list = rd.sample(input_list, list_size)   

    # @return: return the list with randomy select items
    return input_list
     
def sort_selective(list_in):
    ##
    # Function able to sort a list with the selective way
    # @param list_in: the input list to be sorted
    
    # First check if provided list is not empty
    if len(list_in)==0:
        raise ValueError('provided list is empty')    
    
    # Initialise variables
    i=0
    min_index=0
    mini=0

    # Compute the sort of the list
    for i in range(len(list_in)):
        mini = min(list_in[i:]) 
        min_index = list_in[i:].index(mini) 
        list_in[i + min_index] = list_in[i] 
        list_in[i] = mini                  
        
    # @return the sorted list
    return list_in
 
# (a) Illustrate the algorithm on the following vector sample : 10, 15, 7, 1, 3, 3, 9
# Done
# (b) Does the number of iterations depend on the vector content ?
# Yes, there are more or less complex situations 
# (c) How many iterations are required to sort the whole vector ?
# Here 7
# (d) How many permutations are applied ?
# There is n swaps, here 7
# (e) How many comparisons are applied ?
# There is n2 comparaisons, here 49
# (f) Can you quantify the algorithm complexity ?
#  O(n2), it's not an effective algorithm for large lists
# (g) Compare the number of permutations and comparisons for input vectors of varying sizes : 50, 100 and 500
# permutations : 50 -> 50, 100->100, 500->500
# comparaisons : 50 -> 2500, 100->10000, 500->250000

def sort_bubble(list_in):
    ##
    # Function able to sort a list with the bubble way

    # First check if provided list is not empty
    if len(list_in)==0:
        raise ValueError('provided list is empty')
        
    # @param list_in: the input list to be sorted
    for nums in range(len(list_in)-1,0,-1):
        for i in range(nums):
            if list_in[i]>list_in[i+1]:
                temp = list_in[i]
                list_in[i] = list_in[i+1]
                list_in[i+1] = temp

    # @return the sorted list
    return list_in

# (a) Illustrate the algorithm on the following vector sample : 10, 15, 7, 1, 3, 3, 9
# Done
# (b) Does the number of iterations depend on the vector content ?
# Yes, depend of the case 
# (c) How many iterations are required to sort the whole vector ?
# 
# (d) How many permutations are applied ?
# n2 permutations, here 49
# (e) How many comparisons are applied ?
# n2 permutations, here 49
# (f) Can you quantify the algorithm complexity ?
# O(n) in best case,  O(n2) in Worst-case performance
# (g) Compare the number of permutations and comparisons for input vectors of varying sizes : 50, 100 and 500
# permutations : 50 -> 2500, 100->10000, 500->250000
# comparaisons : 50 -> 2500, 100->10000, 500->250000