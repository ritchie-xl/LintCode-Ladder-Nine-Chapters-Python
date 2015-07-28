__author__ = 'ritchie'
import unittest
import ch2.find_peak as fp

class findPeakTest(unittest.TestCase):
    def test_1(self):
        A = [1,2,3,2,4,3,5,3]
        B = [3,4,5]
        ret = fp.findPeak(A)
        self.assertIn(ret, B)
