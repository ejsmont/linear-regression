from unittest import TestCase
from data_handler import DataHandler


class TestDataHandler(TestCase):

    def setUp(self):
        self.dataHandler = DataHandler("../resources/small.csv")
        self.dataHandler.load_from_file()

    def test_load_from_file(self):
        self.assertEqual(2, self.dataHandler._size)

    def test_get_train_and_test_sets(self):
        train, test = self.dataHandler.get_train_and_test_sets()
        self.assertListEqual([10.0, 20.0, 20.0], train[0])
        self.assertListEqual([20.0, 20.0, 30.0], test[0])
