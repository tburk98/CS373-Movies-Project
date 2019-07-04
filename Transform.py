import csv
import numpy as np

with open('updated_movie_rating.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    number_of_users = 0
    number_of_movies = 0

    user_set = set()
    movie_set = set()

    i = 0
    for row in csv_reader:

        print(row)

        if (i == 0):
            i = i + 1
            continue

        user_set.add(int(row[0]))
        movie_set.add(int(row[1]))

    #size of the matrix
    number_of_users = max(user_set)
    number_of_movies = max(movie_set)

    print(number_of_users)
    print(number_of_movies)

    matrix = np.zeros((number_of_users, number_of_movies))

    csv_file.seek(0)

    i = 1
    for row in csv_reader:

        if (i == 1):


            i = i + 1
            continue

        matrix[int(row[0])-1,int(row[1])-1] = float(row[2])

    np.savetxt("final_test_data.csv", matrix, fmt="%s", delimiter=',')


    



