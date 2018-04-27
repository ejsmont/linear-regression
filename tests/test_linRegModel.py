from unittest import TestCase
from data_handler import DataHandler
from lin_reg_model import LinRegModel

sol_1 = [0.0, 3.0]


class TestLinRegModel(TestCase):
    def test_train(self):
        handler = DataHandler('../resources/perfect_fit_tiny.csv')
        handler.load_from_file()
        train, _ = handler.get_train_and_test_sets()
        model = LinRegModel()
        model.train(train)
        self.assertListEqual(sol_1, model.get_h())
