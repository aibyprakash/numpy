import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#All 0s matrix
matrix = np.zeros((2,3))

print(matrix)

#All 1s
matrix = np.ones((4,2,2),dtype='int32')
print(matrix)

#Any other number

matrix = np.full((2,2,3),99)
print(matrix)

#Any other number (Full Like)
print(np.full(a.shape,4))
print(np.full_like(a,4))

#Random decimal numbers
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))

#random Integer values
print(np.random.randint(7,size =(3,3)))
print(np.random.randint(4,8,size =(3,3)))
print(np.random.randint(-4,4,size =(3,3)))

#The identity matrix

print(np.identity(5))

arr= np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis =1)
print(r1)

#Problem : To make a matrix given below

'''
 [1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]

'''

#step1 - Initialize a 5x5  matrix with 1s
output = np.ones((5,5))
print(output)

#step2 - Initialize inner matrix with zeros
z=np.zeros((3,3))
#step3 - Replace mid element of the zeros matrix with 9 that is [1,1]
z[1,1]=9
print(z)
#step4 - Add zeros matrix to ones matrix 
output[1:4,1:4]=z #output[1st row to 3rd Row,1st column to 3 column]
print(output)