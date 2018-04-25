class DataHandler(object):
    """
    Class responsible for handling of data used for training and testing models
    """

    def __init__(self, path_str, delimiter=',', split_ratio=0.8):
        self._path_str = path_str
        self._delimiter = delimiter
        self._ratio = split_ratio
        self._train_set = [[], []]
        self._test_set = [[], []]

    def load_from_file(self):
        """
        Loads data from csv file and stores it in training and testing sets by ratio specified during initialization.
        Throws exception if file cannot be open,
        read or the data is corrupted
        """
        pass

    def get_all_data(self):
        """
        Returns training and testing sets as a tuple
        :return: a tuple containing training and testing sets
        """
        return self._train_set, self._test_set
