from unittest import TestCase
from data_handler import DataHandler


class TestDataHandler(TestCase):

    def setUp(self):
        self.dataHandler = DataHandler("../resources/small.csv")
        self.dataHandler.load_from_file()

    def test_load_from_file(self):
        self.assertEqual(10, self.dataHandler._size)
        self.assertListEqual([10.0, 20.0, 20.0], self.dataHandler._train_set[0])
        self.assertListEqual([70.0, 30.0, 35.0], self.dataHandler._test_set[0])
        self.assertEqual(8, len(self.dataHandler._train_set))
        self.assertEqual(2, len(self.dataHandler._test_set))

    def test_split_data(self):
        self.dataHandler.split_data(0.5)
        self.assertListEqual([10.0, 20.0, 20.0], self.dataHandler._train_set[0])
        self.assertListEqual([60.0, 60.0, 60.0], self.dataHandler._test_set[0])
        self.assertEqual(5, len(self.dataHandler._train_set))
        self.assertEqual(5, len(self.dataHandler._test_set))

    def test_get_train_and_test_sets(self):
        train, test = self.dataHandler.get_train_and_test_sets()
        self.assertListEqual([10.0, 20.0, 20.0], train[0])
        self.assertListEqual([70.0, 30.0, 35.0], test[0])
