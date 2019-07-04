import csv
import numpy as np

new_movie_id = dict()

with open('ratings.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    num_rows = 100837
    num_cols = 3

    new_matrix = np.zeros((num_rows, num_cols), int)

    count = 0
    i = -1
    for row in csv_reader:

        if (i == -1):
            
            i = 1
            continue

        current_id = int(row[1])

        #adding the user ID
        new_matrix[i, 0] = int(row[0])    

        #adding the movie ID
        if (current_id in new_movie_id):

            new_matrix[i, 1] = new_movie_id[int(row[1])]

        else:

            new_matrix[i, 1] = count

            new_movie_id[int(row[1])] = count
            count = count + 1

        #addint the movie rating
        new_matrix[i, 2] = float(row[2])

        i = i + 1

np.savetxt("updated_movie_rating.csv", new_matrix, fmt="%s", delimiter=',')
        
#lookup
with open('movies.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    lookup_matrix = np.zeros((9743,))

    i = 0

    for row in csv_reader:

        if (i == 0):
            i = 1
            continue

        #new movie ID    
        if (int(row[0]) in new_movie_id):
            lookup_matrix[i,0] = new_movie_id[int(row[0])]
        
        else:
            continue

        #old movie ID
        lookup_matrix[i,1] = int(row[0])
    
        i = i + 1

    print(lookup_matrix)
    np.savetxt("new_movie_id_lookup.csv", lookup_matrix, fmt="%s", delimiter=',')


    




