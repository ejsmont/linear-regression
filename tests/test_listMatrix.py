from unittest import TestCase
import list_matrix

A = [[1, 2], [3, 4], [5, 6], [7, 8]]
B = [[1], [1]]
C = [[1, 2, 3], [4, 5, 6]]
D = [[1, 2, 3, 4]]
mul_res = [[9, 12, 15], [19, 26, 33], [29, 40, 51], [39, 54, 69]]
c_trans = [[1, 4], [2, 5], [3, 6]]

XY = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
S = [[2], [3], [-1]]

c_with_ones_row = [[1, 1, 1], [1, 2, 3], [4, 5, 6]]
c_with_ones_column = [[1, 1, 2, 3], [1, 4, 5, 6]]

c_stripped = [[1, 2], [4, 5]]


class TestListMatrix(TestCase):

    def test_dim(self):
        self.assertEqual((4, 2), list_matrix.dims(A))
        self.assertEqual((2, 1), list_matrix.dims(B))
        self.assertEqual((2, 3), list_matrix.dims(C))
        self.assertEqual((1, 4), list_matrix.dims(D))

    def test_multiply(self):
        M = list_matrix.multiply(A, C)
        self.assertListEqual(mul_res, M)
        self.assertEqual((4, 3), list_matrix.dims(M))

    def test_transpose(self):
        T = list_matrix.transpose(C)
        self.assertListEqual(c_trans, T)
        self.assertEqual((3, 2), list_matrix.dims(T))

    def test_gaussian(self):
        self.assertListEqual(S, list_matrix.gaussian_elimination(XY))

    def test_add_ones_row(self):
        self.assertListEqual(c_with_ones_row, list_matrix.add_ones_row(C))

    def test_add_ones_column(self):
        self.assertListEqual(c_with_ones_column, list_matrix.add_ones_column(C))

    def test_remove_last_column(self):
        self.assertListEqual(c_stripped, list_matrix.remove_last_column(C))
