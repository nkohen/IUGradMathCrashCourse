import unittest
from main import *
import math
import random

class Test(unittest.TestCase):
    def test_euclid(self):
        for i in range(1000):
            num1 = random.randint(1,1000)
            num2 = random.randint(1,1000)
            self.assertEqual(euclid_loop(num1,num2,min(num1,num2)),math.gcd(num1,num2))

    def test_inverse(self):
        self.assertEqual(modular_inverse_loop(7 % 8, 8, 8, 1, None, None, None, None),7)
        self.assertEqual(modular_inverse_loop(3 % 11, 11, 11, 1, None, None, None, None),4)
        self.assertEqual(modular_inverse_loop(16 % 12, 12, 12, 1, None, None, None, None), False)

if __name__ == '__main__':
    unittest.main()