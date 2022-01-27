import unittest
from main import *

def f1(n):
    return n
def f2(n):
    return n ** s2
def f3(n):
    return 3-n

class MyTestCase(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(intersection([1,2,4,3,1,-1],["a","b",-1,-1,True]),{True,-1})
        self.assertEqual(intersection([1,0,"a","b","b","c",4],[0,0,"c","a",-1]),{0,"a","c"})

    def test_func_intersection(self):
        self.assertEqual(func_intersection(f1,f2,9),{0,1,4,9})
        self.assertEqual(func_intersection(f1, f3, 10), {3,2,1,0})

if __name__ == '__main__':
    unittest.main()
