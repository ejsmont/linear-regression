if __name__ == '__main__':
    from lin_reg_model import LinRegModel
    from data_handler import DataHandler
    # load data
    handler = DataHandler('./resources/power_plant.csv', delimiter=',')
    handler.load_from_file()
    # split in training and testing
    handler.split_data(0.8)
    train, test = handler.get_train_and_test_sets()
    # train the lin reg model
    model = LinRegModel()
    model.train(train)
    h = model.get_h()
    print(h)
    # use model to predict on test
    model.predict(test)
    p = model.get_predictions()
    #show results
    counter = 0
    for actual, predicted in zip(test, p):
        print("actual : ", actual[-1], ' ---- ', predicted[0], " : predicted")
        counter += 1
        if counter == 10:
            break
