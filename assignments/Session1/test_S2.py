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
    
    # Initialise test list   
    test_list=[1,2,3,4,-7]
    test_reversed_list=[-7,4,3,2,1]
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