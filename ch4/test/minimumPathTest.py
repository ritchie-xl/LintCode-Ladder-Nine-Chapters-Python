__author__ = 'lei'

import unittest
from ch4.minimum_path_sum import minPathSum as mps


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = [
            [1,2,3],
            [1,2,3]
        ]
        self.assertEqual(mps(a), 7)

if __name__ == '__main__':
    unittest.main()

