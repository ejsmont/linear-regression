from unittest import TestCase
from list_matrix import ListMatrix

A = [[1, 2], [3, 4]]
B = [[1], [1]]
C = [[1, 2, 3], [4, 5, 6]]


class TestListMatrix(TestCase):

    def test_dim(self):
        self.assertEquals((2, 2), ListMatrix.dims(A))
        self.assertEquals((2, 1), ListMatrix.dims(B))
        self.assertEquals((2, 3), ListMatrix.dims(C))
