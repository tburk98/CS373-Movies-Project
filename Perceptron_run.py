import numpy as np
import csv
from sklearn.svm import SVC 
import sol_linperceptron as perceptron
import sol_linpred as linpred

testing_movie = 20
cutoff = 3

with open('final_test_data.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    _list = list(csv_reader)
    data = np.array(_list).astype("float")

    n, d = data.shape
    
    for i in range(n):

        for j in range(d):

            if (data[i][j] == 0):

                data[i][j] = 0

            elif (data[i][j] > cutoff):
            
                data[i][j] = 1
            else:
                
                data[i][j] = -1

    X = np.zeros((n, d-1), dtype="int")

    X = data[:,range(21,d)]

    y = data[:, testing_movie]

    #y = np.resize(y, (n, 1))

    theta = perceptron.run(10,X,y)

    running_sum = 0.0
    for i in range(n):

        test = linpred.run(theta, X[i])

        if (test != y[i] and y[i] != 0):
            running_sum += 1

    print(running_sum/n)



    # alg = SVC(C=1, kernel='linear')
    # alg.fit(X, y)
    # y_pred= alg.predict(X)
    # err = np.mean(y!=y_pred)

    # print(err)
