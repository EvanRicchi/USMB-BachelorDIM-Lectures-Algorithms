# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:48:11 2017

@author: ricchie
"""

import S1_algotools as algo
import pytest

def test_average_above_zero():
    ##
    # Basic function able to test average_above_zero function

    test_list=[1,2,3,4,-7]
    assert algo.average_above_zero(test_list) == 2.5
    
    test_list=[2,4,8,16,32]
    assert algo.average_above_zero(test_list) == 12.4
    
    test_list=[-2,-4,-8,-16,-32,1]
    assert algo.average_above_zero(test_list) == 1.0
    
    test_list=[-2,-4,-8,-16,-32,-1]
    with pytest.raises(ZeroDivisionError):
        algo.average_above_zero(test_list)
        
    test_list=[0,0,0]
    with pytest.raises(ZeroDivisionError):
        algo.average_above_zero(test_list)
    
def test_max_value():
    ##
    # Basic function able to test max_value function
    
    test_list=[1,2,3,4,-7]
    assert algo.max_value(test_list) == 4
    
    test_list=[2,4,8,16,32]
    assert algo.max_value(test_list) == 32
    
    test_list=[-2,-4,-8,-16,-32]
    assert algo.max_value(test_list) == -2
    
    test_list=[0, 0, 0]
    assert algo.max_value(test_list) == 0
    
def test_reverse_table():
    ##
    # Basic function able to test reverse_table function
    
    test_list=[1,2,3,4,-7]
    algo.max_value(test_list) == [-7,4,3,2,1]
    
    