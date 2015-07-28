__author__ = 'ritchie'
import unittest
import ch2.binary_search as bs

class binarySearchTest(unittest.TestCase):
    def test_1(self):
        a = []
        b = 1
        self.assertEquals(bs.binarySearch(a,b),-1)

    def test_2(self):
        a = []
        b = None
        self.assertEquals(bs.binarySearch(a,b),-1)

    def test_3(self):
        a = [1,2,3,4,5,6,7]
        b = 1
        self.assertEquals(bs.binarySearch(a,b),0)

    def test_4(self):
        a = [1,2,3,4,5,6,7]
        b = 7
        self.assertEquals(bs.binarySearch(a,b),6)

    def test_5(self):
        a = [1,2,3,4,5,6,7]
        b = 3
        self.assertEquals(bs.binarySearch(a,b),2)

    def test_6(self):
        a = [3,4,5,8,8,8,8,10,13,14]
        b = 8
        self.assertEquals(bs.binarySearch(a,b),3)