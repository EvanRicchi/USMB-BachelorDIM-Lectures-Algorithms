# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:48:11 2017

@author: ricchie
"""

import S1_algotools as algo
import pytest
import numpy as np
from numpy.testing import assert_array_equal

def test_average_above_zero():
    ##
    # Basic function able to test average_above_zero function
    
    # Testing with a random classic list
    test_list=[1,2,3,4,-7]
    assert algo.average_above_zero(test_list) == 2.5

    test_list=[2,4,8,16,32]
    assert algo.average_above_zero(test_list) == 12.4
    
    # Testing with a negative value list and a positive value
    test_list=[-2,-4,-8,-16,-32,1]
    assert algo.average_above_zero(test_list) == 1.0
    
    # Testing with a list of negative values (Raise exception)
    test_list=[-2,-4,-8,-16,-32,-1]
    with pytest.raises(ZeroDivisionError):
        algo.average_above_zero(test_list)
    
    # Testing with a list of 0 (Raise exception)
    test_list=[0,0,0]
    with pytest.raises(ZeroDivisionError):
        algo.average_above_zero(test_list)
    
def test_max_value():
    ##
    # Basic function able to test max_value function

    # Testing with an empty list
    test_list=[]
    with pytest.raises(ValueError):
        algo.max_value(test_list)
    
    # Testing with a random classic list
    test_list=[1,2,3,4,-7]
    assert algo.max_value(test_list) == 4
    
    # Testing with a list of positive values
    test_list=[2,4,8,16,32]
    assert algo.max_value(test_list) == 32
    
    # Testing with a list of negative values
    test_list=[-2,-4,-8,-16,-32]
    assert algo.max_value(test_list) == -2
    
    # Testing with a list of 0
    test_list=[0, 0, 0]
    assert algo.max_value(test_list) == 0
    
def test_reverse_table():
    ##
    # Basic function able to test reverse_table function
    
    # Testing with an empty list
    test_list=[]
    with pytest.raises(ValueError):
        algo.reverse_table(test_list)
    
    # Initialise test list   
    test_list=[1,2,3,4,-7]
    test_reversed_list=[-7,4,3,2,1]
    
    # Testing with a basic list
    assert algo.reverse_table(test_list) == test_reversed_list
    
def test_roi_bbox():
    ##
    # Basic function able to test roi_bbox function

    # Initialise a numpy array of test    
    size_rows=10
    size_cols=10
    myMat=np.zeros([size_rows, size_cols], dtype=int)
    myMat[2:4,5:9]=np.ones([2,4])
    test_numpy_array = np.array([[5,2],[8,2],[5,8],[8,3]])
    
    # Using assert_array_equal function from numpy to compare 2 numpy array
    assert_array_equal(algo.roi_bbox(myMat),test_numpy_array)
    
def test_shuffle():
    ##
    # Basic function able to test shuffle function
    
    # Testing with an empty list
    test_list=[]
    with pytest.raises(ValueError):
        algo.shuffle(test_list)
        
    # Initialise test list    
    test_list=[1,2,3]
    # Test all the possibilities with a shuffle
    assert algo.shuffle(test_list) == [1,2,3] or [2,1,3] or [2,3,1] or [1,3,2] or [3,1,2] or [3,2,1]

def test_remove_whitespace():
    ##
    # Basic function able to test remove_whitespace function
    
    # Testing with an empty string
    test_string=""
    with pytest.raises(ValueError):
        algo.remove_whitespace(test_string)
        
    # Initialise test string    
    test_string="This is a test 1 2 3"
    # Test with a ordinary string
    assert algo.remove_whitespace(test_string) == "Thisisatest123"
    
    # Initialise test string    
    test_string="Thisisatest123"
    # Test with a string without whitespaces
    assert algo.remove_whitespace(test_string) == "Thisisatest123"
    
def test_sort_selective():
    ##
    # Basic function able to test sort_selective function

    # Testing with an empty list
    test_list=[]
    with pytest.raises(ValueError):
        algo.sort_selective(test_list)
    
    # Initialise test list    
    test_list=[10, 15, 7, 1, 3, 3, 9]
    # Test with a ordinary list
    assert algo.sort_selective(test_list) == [1, 3, 3, 7, 9, 10, 15]
    
    # Initialise test list    
    test_string=[-10, -15, -7, -1, -3, -3, -9]
    # Test with a list of negative values
    assert algo.sort_selective(test_string) == [-15, -10, -9, -7, -3, -3, -1]

def test_sort_bubble():
    ##
    # Basic function able to test sort_bubble function

    # Testing with an empty list
    test_list=[]
    with pytest.raises(ValueError):
        algo.sort_bubble(test_list)
    
    # Initialise test list    
    test_list=[10, 15, 7, 1, 3, 3, 9]
    # Test with a ordinary list
    assert algo.sort_bubble(test_list) == [1, 3, 3, 7, 9, 10, 15]
    
    # Initialise test list    
    test_string=[-10, -15, -7, -1, -3, -3, -9]
    # Test with a list of negative values
    assert algo.sort_bubble(test_string) == [-15, -10, -9, -7, -3, -3, -1]

def test_random_fill_sparse():
    ##
    # Basic function able to test random_fill_sparse function

    input_array=np.chararray((10, 10))
    input_array[:] = ''
    vfill= input_array.size
    alea = algo.random(vfill)
    result = algo.random_fill_sparse(input_array,alea)