__author__ = 'ritchie'
import unittest
import ch1.recover_rotated_sorted_array as rsa

class recoverRotatedSortedArray(unittest.TestCase):
    def test_1(self):
        a = [4,5,1,2,3]
        b = rsa.Solution()
        b.recoverRotatedSortedArray(a)
        self.assertEqual(a,[1,2,3,4,5])