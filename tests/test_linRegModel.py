from unittest import TestCase
from data_handler import DataHandler
from lin_reg_model import LinRegModel

sol_1 = [[0.0], [3.0]]
pred_1 = [[12.0]]


class TestLinRegModel(TestCase):
    def setUp(self):
        self._dataHandler = DataHandler('../resources/perfect_fit_tiny.csv')
        self._dataHandler.load_from_file()
        self._model = LinRegModel()
        self._model.train(self._dataHandler._train_set)
        self._model.predict(self._dataHandler._test_set)

    def test_train(self):
        self.assertListEqual(sol_1, self._model.get_h())

    def test_predict(self):
        self.assertListEqual(pred_1, self._model.get_predictions())
