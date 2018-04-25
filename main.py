if __name__ == '__main__':
    from data_handler import DataHandler
    handler = DataHandler('./resources/small.csv')
    handler.load_from_file()
    # load data

    # split in training and testing
    # train the lin reg model
    # use model to predict on test
    # check correctness
