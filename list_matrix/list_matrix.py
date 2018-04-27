# TODO - refactor and make it a class that keeps the original matrix

def multiply(a, b):
    """
    Multiplies two matrices. Returns a product matrix.
    :param a: first operand (matrix)
    :param b: second operand (matrix)
    :return: result of matrix multiplication
    """
    a_n, a_m = dims(a)
    b_n, b_m = dims(b)
    assert a_m == b_n
    return [[sum([a[i][k] * b[k][j] for k in range(a_m)]) for j in range(b_m)] for i in range(a_n)]


def dims(a):
    """
    Computes dimensions of a provided matrix recursively
    :param a: matrix to check dimensions on
    :return: a tuple containing dimensions of a matrix
    """
    if not type(a) == list:
        return tuple()
    return (len(a),) + dims(a[0])


def transpose(a):
    """
    Returns a transposed matrix
    :param a: matrix to be transposed
    :return: transposed matrix
    """
    d_n, d_m = dims(a)
    return [[a[i][j] for i in range(d_n)] for j in range(d_m)]


def gaussian_elimination(a):
    """
    Algorithm for solving linear equation using gaussian elimination method. Does not modify input matrix.
    The algorithm is a slight modification of the one found here:
    https://martin-thoma.com/solving-linear-equations-with-gaussian-elimination/

    :param a: a matrix containing system of linear equations of dimensions n, n+1
    :return: a list containing solution for given system of linear equations
    """
    n, d_m = dims(a)
    assert n + 1 == d_m
    import copy
    a = copy.deepcopy(a)
    for i in range(n):
        max_el = abs(a[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(a[k][i]) > max_el:
                max_el = abs(a[k][i])
                max_row = k
        temp = a[max_row]
        a[max_row] = a[i]
        a[i] = temp
        for k in range(i + 1, n):
            c = -a[k][i] / a[i][i]
            for j in range(i, n + 1):
                if j == i:
                    a[k][j] = 0
                else:
                    a[k][j] += c*a[i][j]
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = round(a[i][n]/a[i][i], 10)
        for k in range(i - 1, -1, -1):
            a[k][n] -= a[k][i]*x[i]
    return x


def add_ones_row(a):
    """
    Adds row of ones as a first row
    :param a: matrix to which copy ones row will be added
    :return: copy of matrix a with ones row added
    """
    _, d_m = dims(a)
    return [[1 for _ in range(d_m)]] + a


def add_ones_column(a):
    """
    Adds column of ones as a first column
    :type a: list
    :param a: matrix to which copy ones column will be added
    :return: copy of matrix a with ones column added
    """
    d_n, _ = dims(a)
    return [[1] + row for row in a]


def remove_last_column(a):
    """
    Returns copy of input matrix with the last column removed
    :param a: matrix to be modified
    :return: modified matrix
    """
    return [row[:-1] for row in a]