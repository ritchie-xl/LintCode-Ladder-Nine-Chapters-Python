__author__ = 'ritchie'
import ch2.search_for_range as sr
import unittest

class searchForRangeTest(unittest.TestCase):
    def test_1(self):
        A = []
        b = None
        self.assertEquals(sr.searchRange(A,b),[-1,-1])

    def test_2(self):
        A = [1,2,3,4,4,4,5,6]
        b = 4
        self.assertEquals(sr.searchRange(A,b),[3,5])

    def test_3(self):
        A = [1,10,1001,201,1001,10001,10007]
        b = 10008
        self.assertEquals(sr.searchRange(A,b),[-1,-1])

    def test_4(self):
        A = []
        b = 9
        self.assertEquals(sr.searchRange(A,b),[-1,-1])