#this lets you impprt something from antoher file! from ( file name) import (finction you want)
from in_class_1_31 import compute_triangl_area

def test_compute_triangl_area(): 
    assert compute_triangl_area(5,6) == 15
    assert compute_triangl_area(50500, 62245) == 1571686250

