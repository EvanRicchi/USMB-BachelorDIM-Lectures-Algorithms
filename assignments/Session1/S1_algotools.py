# -*- coding: utf-8 -*-
##
#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : a set of generic functions for data management

# Function for compute the average of the positive elements of a table.
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

# Function to get the maximum value of a table
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
    # Compute the max value elements of a list
    for item in input_list:
        # Select only positive items
        if max_val<item:
            max_val=item
    return max_val

# Testing max value function :
mylist2=[-1,2,-20]
result2=max_value(mylist2)
message='Max value of {input_list} is {max_scan}'.format(input_list=mylist2,max_scan=result2)
print(message)