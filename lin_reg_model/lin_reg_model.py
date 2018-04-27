import list_matrix


class LinRegModel(object):
    """
    Class responsible for providing linear regression model using least squares modelling.
    """

    def __init__(self):
        self._h = []

    def get_h(self):
        return self._h

    def train(self, data):
        """
        Trains the model on provided data using least squares matrix manipulation.
        It is expected that data contains both target variable (right most column)

        :param data: data (matrix) containing both input and target variables for observations
        :return: list containing fitted parameters a_i of form [a_0, a_1 ... a_n]
                    where n is the number of unique features
        """
        # create a new matrix with additional column (first column) with ones
        with_ones = list_matrix.add_ones_column(data)
        # transpose extended matrix and strip row with target values
        transposed = list_matrix.transpose(with_ones)[:-1]
        # find the coefficients using matrix multiplication
        coefficients = list_matrix.multiply(transposed, with_ones)
        # solve
        self._h = list_matrix.gaussian_elimination(coefficients)
