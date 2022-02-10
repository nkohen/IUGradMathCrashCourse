import unittest
from main import *
import random
import numpy as np

def random_matrix(dim):
    matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(random.randint(-20,20))
        matrix.append(row)
    return matrix

class Testing(unittest.TestCase):
    def test_det(self):
        dim = random.randint(1,5)
        mat = random_matrix(dim)
        # Checking against NumPy's determinant function
        self.assertEqual(det(mat),round(np.linalg.det(mat)))

    def test_first_minor(self):
        mat = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(first_minor([[1,1,1,1],
                                      [1,0,0,0],
                                      [1,0,0,0],
                                      [1,0,0,0]],
                                     0,0),
                         mat)
        self.assertEqual(first_minor([[0,0,1,0],
                                      [1,1,1,1],
                                      [0,0,1,0],
                                      [0,0,1,0]],
                                     1,2),
                         mat)
        self.assertEqual(first_minor([[0,0,0,1],
                                      [0,0,0,1],
                                      [0,0,0,1],
                                      [1,1,1,1]],
                                     3,3),
                         mat)
        self.assertEqual(first_minor([[2, -3, 0, 1],
                                      [-2, 1, 3, 1],
                                      [0, -4, -2, 1],
                                      [-4, 2, 3, 1]],
                                     2, 0),
                         [[-3, 0, 1],
                          [1, 3, 1],
                          [2, 3, 1]])

if __name__ == '__main__':
    unittest.main()
