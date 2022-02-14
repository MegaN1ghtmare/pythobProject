from array_increment import *
from array_reverse import *
from array_print_reverse import *
from array_search import *
from gcd import *
import math


def test_array_print():
    arr = [1, 2, 3, 4, 6]
    array_print(arr)

    assert '1 2 3 4 6'


def test_array_print_reverse():
    arr = [1, 2, 3, 4, 6]
    array_reverse_print(arr)

    assert '6 4 3 2 1'


def test_array_reverse():
    arr = [0, -2, 7, 4, 6, 11]
    array_reverse(arr)

    assert arr == [11, 6, 4, 7, -2, 0]


def test_array_increment():
    arr = [1, 2, 3, 4, 6]
    array_increment(arr, 3)

    assert arr == [4, 5, 6, 7, 9]


def test_array_search():
    arr = [1, 2, 3, 4, 6]

    assert array_search_elem_index(arr, 3) == 2
    assert array_search_elem_index(arr, 6) == 4
    assert array_search_elem_index(arr, 1) == 0


def test_gcd():
    assert gcd_function(2, 10) == math.gcd(2, 10)
    assert gcd_function(201, 101) == math.gcd(201, 101)
    assert gcd_function(-7, 10) == math.gcd(-7, 10)
