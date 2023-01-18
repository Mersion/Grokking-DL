from elementwise_multiplication_addition import neural_network

toes = [8.5, 9.5, 10, 9]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
weights = [[[0.1, 0.2, 0.003],[0.8,0.6,0.7],[1.1,1.2,0.3]],
           [[0.24,0.54,0.67],[0.77,0.98,1],[1.03,1.07,1.11]]]
input = [toes[0], wlrec[0], nfans[0]]
# średnia ważona wiersza 0 - hidden0
# średnia ważona wiersza 0 - hidden1
# średnia ważona wiersza 0 - hidden2

pred = neural_network(input, weights[0])
hid = neural_network(pred, weights[1])

import numpy as np

a = np.array([0,1,2,3]) # a vector
b = np.array([4,5,6,7]) # another vector
c = np.array([[0,1,2,3], # a matrix
              [4,5,6,7]])

d = np.zeros((2,4)) # (2x4 matrix of zeros)
e = np.random.rand(2,5) # random 2x5
# matrix with all numbers between 0 and 1

print(a)
print(b)
print(c)
print(d)
print(e)
print(a * 0.1) # multiplies every number in vector "a" by 0.1
      
print(c * 0.2) # multiplies every number in matrix "c" by 0.2
      
print(a * b) # multiplies elementwise between a and b (columns paired up)
      
print(a * b * 0.2) # elementwise multiplication then multiplied by 0.2
      
print(a * c) # since c has the same number of columns as a, this performs
# elementwise multiplication on every row of the matrix "c"

print(a * e) # since a and e don't have the same number of columns, this
# throws a "Value Error: operands could not be broadcast together with.."
