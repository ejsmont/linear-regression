from unittest import TestCase
from list_matrix import ListMatrix

A = [[1, 2], [3, 4], [5, 6], [7, 8]]
B = [[1], [1]]
C = [[1, 2, 3], [4, 5, 6]]
mul_res = [[9, 12, 15], [19, 26, 33], [29, 40, 51], [39, 54, 69]]
c_trans = [[1, 4], [2, 5], [3, 6]]


class TestListMatrix(TestCase):

    def test_dim(self):
        self.assertEqual((4, 2), ListMatrix.dims(A))
        self.assertEqual((2, 1), ListMatrix.dims(B))
        self.assertEqual((2, 3), ListMatrix.dims(C))


class TestListMatrix(TestCase):
    def test_multiply(self):
        M = ListMatrix.multiply(A, C)
        self.assertListEqual(mul_res, M)
        self.assertEqual((4, 3), ListMatrix.dims(M))

class TestListMatrix(TestCase):
    def test_transpose(self):
        T = ListMatrix.transpose(C)
        self.assertListEqual(c_trans, T)
        self.assertEqual((3, 2), ListMatrix.dims(T))
