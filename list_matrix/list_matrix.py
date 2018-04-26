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
        Multiplies two matrices. Return the product.
        :param a: first operand (matrix)
        :param b: second operand (matrix)
        :return: result of matrix multiplication
        """
        dims_a = ListMatrix.dims(a)
        dims_b = ListMatrix.dims(b)
        assert dims_a[1] == dims_b[0]
