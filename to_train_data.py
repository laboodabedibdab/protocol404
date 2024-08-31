import random

import scipy.io.wavfile as wav
import numpy as np
import os
def load_data():
    train = []
    test_X = []
    directory_404 = os.fsencode("404")

    for file in os.listdir(directory_404):
        filename = os.fsdecode(file)
        train.append((wav.read("404/"+filename)[1].tolist(),1))

    directory_noth = os.fsencode("noth")

    for file in os.listdir(directory_noth):
        filename = os.fsdecode(file)
        train.append((wav.read("noth/"+filename)[1].tolist(),0))

    directory_test_404 = os.fsencode("test_404")
    t4 = len(os.listdir(directory_test_404))
    for file in os.listdir(directory_test_404):
        filename = os.fsdecode(file)
        test_X.append(wav.read("test_404/" + filename)[1].tolist())

    directory_test_noth = os.fsencode("test_noth")
    tn = len(os.listdir(directory_test_noth))
    for file in os.listdir(directory_test_noth):
        filename = os.fsdecode(file)
        test_X.append(wav.read("test_noth/" + filename)[1].tolist())

    random.shuffle(train)
    train_X = np.array(list(map(lambda x:x[0], train)))
    train_Y = np.array(list(map(lambda x:x[1], train)))
    print(test_X)
    test_X = np.array(test_X)
    test_Y = np.array([1 for _ in range(t4)] + [0 for _ in range(tn)])
    return train_X, train_Y, test_X, test_Y
