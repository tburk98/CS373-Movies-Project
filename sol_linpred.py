# Input: numpy vector theta of d rows, 1 column
#        numpy vector x of d rows, 1 column
# Output: label (+1 or -1)
def run(theta, x):
    import numpy as np
    dotp = np.dot(theta.T, x)
    if dotp > 0:
        return 1.
    else:
        return -1.