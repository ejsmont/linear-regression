from unittest import TestCase
from list_matrix import ListMatrix

A = [[1, 2], [3, 4], [5, 6], [7, 8]]
B = [[1], [1]]
C = [[1, 2, 3], [4, 5, 6]]
mul_res = [[9, 12, 15], [19, 26, 33], [29, 40, 51], [39, 54, 69]]


class TestListMatrix(TestCase):

    def test_dim(self):
        self.assertEquals((4, 2), ListMatrix.dims(A))
        self.assertEquals((2, 1), ListMatrix.dims(B))
        self.assertEquals((2, 3), ListMatrix.dims(C))


class TestListMatrix(TestCase):
    def test_multiply(self):
        self.assertListEqual(mul_res, ListMatrix.multiply(A, C))

