import unittest
from main import *
import math
import random

class Test(unittest.TestCase):
    def test_euclid(self):
        for i in range(1000):
            num1 = random.randint(1,1000)
            num2 = random.randint(1,1000)
            self.assertEqual(euclid(num1,num2),math.gcd(num1,num2))

if __name__ == '__main__':
    unittest.main()