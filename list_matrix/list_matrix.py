class ListMatrix(object):
    """
    Class responsible for typical two dimensional matrix operations represented as two dimensional
    python lists.
    """

    @staticmethod
    def dims(a):
        """
        Computes dimensions of a provided matrix recursively
        :param a: matrix to check dimensions on
        :return: a tuple containing dimensions of a matrix
        """
        if not type(a) == list:
            return tuple()
        return (len(a),) + ListMatrix.dims(a[0])

    @staticmethod
    def multiply(a, b):
        """
        Multiplies two matrices. Returns a product matrix.
        :param a: first operand (matrix)
        :param b: second operand (matrix)
        :return: result of matrix multiplication
        """
        a_n, a_m = ListMatrix.dims(a)
        b_n, b_m = ListMatrix.dims(b)
        assert a_m == b_n
        return [[sum([a[i][k] * b[k][j] for k in range(a_m)]) for j in range(b_m)] for i in range(a_n)]

    @staticmethod
    def transpose(a):
        """
        Returns a transposed matrix
        :param a: matrix to be transposed
        :return: transposed matrix
        """
        d_n, d_m = ListMatrix.dims(a)
        return [[a[i][j] for i in range(d_n)] for j in range(d_m)]