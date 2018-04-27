import list_matrix


class LinRegModel(object):
    """
    Class responsible for providing linear regression model using least squares modelling.
    """

    def __init__(self):
        self._h = []
        self._predictions = []

    def get_h(self):
        return self._h

    def get_predictions(self):
        return self._predictions

    def train(self, data):
        """
        Trains the model on provided data using least squares matrix manipulation.
        It is expected that data contains both target variable (right most column).
        List containing fitted parameters a_i is of form [a_0, a_1 ... a_n]
        where n is the number of unique features

        :param data: data (matrix) containing both input and target variables for observations
        """
        # create a new matrix with additional column (first column) with ones
        with_ones = list_matrix.add_ones_column(data)
        # transpose extended matrix and strip row with target values
        transposed = list_matrix.transpose(with_ones)[:-1]
        # find the coefficients using matrix multiplication
        coefficients = list_matrix.multiply(transposed, with_ones)
        # solve
        self._h = list_matrix.gaussian_elimination(coefficients)

    def predict(self, data):
        """
        Predicts the target values given available computed hypothesis and test data.

        :param data: set on which prediction will be made
        """
        assert len(self._h) != 0
        # add ones column
        with_ones = list_matrix.add_ones_column(data)
        # remove target column
        stripped = list_matrix.remove_last_column(with_ones)
        # calculate predictions
        self._predictions = list_matrix.multiply(stripped, self._h)
