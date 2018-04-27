class DataHandler(object):
    """
    Class responsible for handling of data used for training and testing models
    """

    def __init__(self, path_str, delimiter=',', split_ratio=0.8):
        self._path_str = path_str
        self._delimiter = delimiter
        self._ratio = split_ratio
        self._data = []
        self._size = 0
        self._train_set = []
        self._test_set = []

    def load_from_file(self):
        """
        Loads data from csv file and stores it in training and testing sets by ratio specified during initialization.
        Throws exception if file cannot be open,
        read or the data is corrupted
        """
        with open(self._path_str) as csv_file:
            import csv
            reader = csv.reader(csv_file, delimiter=self._delimiter)
            self._data = [list(map(float, row)) for row in reader]
        self._size = len(self._data)
        self.split_data(self._ratio)

    def split_data(self, ratio):
        """
        Splits data set into two sets using given ratio
        :param ratio: float specifying the ratio
        """
        left_size = int(ratio*self._size)
        self._train_set = self._data[:left_size]
        self._test_set = self._data[left_size:]

    def get_train_and_test_sets(self):
        """
        Returns training and testing sets as a tuple
        :return: a tuple containing training and testing sets
        """
        return self._train_set, self._test_set
