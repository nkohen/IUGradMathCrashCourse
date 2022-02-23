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

    def test_inverse(self):
        self.assertEqual(modular_inverse(7,8),"The inverse of 7 mod 8 is 7")
        self.assertEqual(modular_inverse(3,11),"The inverse of 3 mod 11 is 4")
        self.assertEqual(modular_inverse(4,12),"4 does not have an inverse mod 12")

if __name__ == '__main__':
    unittest.main()