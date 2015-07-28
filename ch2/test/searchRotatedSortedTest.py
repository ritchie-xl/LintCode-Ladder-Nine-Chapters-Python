__author__ = 'ritchie'
import unittest
import ch2.search_rotated_array as sra

class searchRotatedSortedTest(unittest.TestCase):
    def test_1(self):
        A = []
        b = None
        self.assertEquals(sra.search(A,b), -1)

    def test_2(self):
        A = None
        b = 9
        self.assertEquals(sra.search(A,b), -1)

    def test_3(self):
        A = None
        b = None
        self.assertEquals(sra.search(A,b), -1)

    def test_4(self):
        A = [4,5,1,2,3]
        b = 4
        self.assertEquals(sra.search(A,b), 0)

    def test_5(self):
        A = [4,5,1,2,3]
        b = 2
        self.assertEquals(sra.search(A,b), 3)

    def test_6(self):
        A = [4,5,1,2,3]
        b = 3
        self.assertEquals(sra.search(A,b), 4)

    def test_7(self):
        A = [4,5,1,2,3]
        b = 6
        self.assertEquals(sra.search(A,b), -1)