import main
import io
import sys
import re
import math
import types


def test_main_1():
    mylist = [5, 10, 15, 25, 20, 55, 40]
    ret = main.gtLeft(mylist)
    print(f'Return value is {ret}')
    assert isinstance(ret, list)
    assert len(ret) == 4
    assert ret == [10, 15, 25, 55]


def test_main_2():
    mylist = [5, 4, 3, 2, 1]
    ret = main.gtLeft(mylist)
    print(f'Return value is {ret}')
    assert isinstance(ret, list)
    assert len(ret) == 0
    assert ret == []
