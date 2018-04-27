if __name__ == '__main__':
    from lin_reg_model import LinRegModel
    from data_handler import DataHandler
    # load data
    handler = DataHandler('./resources/Daily_Demand_Forecasting_Orders.csv', delimiter=';')
    handler.load_from_file()
    # split in training and testing
    handler.split_data(0.7)
    train, test = handler.get_train_and_test_sets()
    print(train)
    # train the lin reg model
    h = LinRegModel.train(train)
    print(h)
    # use model to predict on test
    # check correctness

