__author__ = 'ritchie'
import unittest
import ch1.strStr as strStr

class strStrTest(unittest.TestCase):
    def test_1(self):
        a = 'abcdcdefgh'
        b ='bcd'
        self.assertEqual(strStr.strStr_2(a,b),1)

    def test_2(self):
        a = ''
        b = ''
        self.assertEqual(strStr.strStr_2(a,b),0)

    def test_3(self):
        a = None
        b = 'abcd'
        self.assertEqual(strStr.strStr_2(a,b),-1)

    def test_4(self):
        a = 'abcd'
        b = ''
        self.assertEqual(strStr.strStr_2(a,b),0)

    def test_5(self):
        a ='abcd'
        b ='ab'
        self.assertEqual(strStr.strStr_2(a,b),0)

    def test_6(self):
        a = 'abcdef'
        b = 'bcd'
        self.assertEquals(strStr.strStr_3(a,b),True)

    def test_7(self):
        a = 'abcdef'
        b = 'bcdf'
        self.assertEquals(strStr.strStr_3(a,b),False)

if __name__ == '__main__':
    unittest.main()