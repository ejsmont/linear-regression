from unittest import TestCase
import list_matrix

A = [[1, 2], [3, 4], [5, 6], [7, 8]]
B = [[1], [1]]
C = [[1, 2, 3], [4, 5, 6]]
mul_res = [[9, 12, 15], [19, 26, 33], [29, 40, 51], [39, 54, 69]]
c_trans = [[1, 4], [2, 5], [3, 6]]


class TestListMatrix(TestCase):

    def test_dim(self):
        self.assertEqual((4, 2), list_matrix.dims(A))
        self.assertEqual((2, 1), list_matrix.dims(B))
        self.assertEqual((2, 3), list_matrix.dims(C))

    def test_multiply(self):
        M = list_matrix.multiply(A, C)
        self.assertListEqual(mul_res, M)
        self.assertEqual((4, 3), list_matrix.dims(M))

    def test_transpose(self):
        T = list_matrix.transpose(C)
        self.assertListEqual(c_trans, T)
        self.assertEqual((3, 2), list_matrix.dims(T))


