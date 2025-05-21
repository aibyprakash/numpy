import numpy as np

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

print(np.matmul(a,b))


#Find the determinant
c= np.identity(3)
print(np.linalg.det(c))

#numpy.org/doc/stable/reference/routines.linalg.html
#Determinant
#Trace
#Singular Vector Decomposition
#Eigenvalues
#Matrix Norm
#Inverse
#Etc . . .

#Statistics in numpy

stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.max(stats))
print(np.max(stats,axis=0))
print(np.max(stats,axis=1))

#Reorganizing arrays

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape(2,4)

#Vertically stacking vectors

v1= np.array([1,2,3,4])
v2= np.array([5,6,7,8])

print(np.vstack([v1,v2,v1,v2]))

#Horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(np.hstack((h1,h2)))


#Miscellaneous


#Load data from file

filedata=np.genfromtxt('data.txt',delimiter=',')
filedata=filedata.astype('int32')
print(filedata)


#Boolean Masking and Advanced indexing
#print(filedata>50)
print(filedata[filedata>50])
#You can index with a list in NumPy
np.array([1,2,3,4,5,6,7,8,9])
print(np.any(filedata>50,axis=0))
print((filedata >50)& (filedata <100))
#Reverse
print(~((filedata >50)& (filedata <100)))


#problem.png solution
matrix = np.arange(1,31).reshape((6,5))
print(matrix[2:4,0:2])
print(matrix[[0,1,2,3],[1,2,3,4]])
print(matrix[[0,4,5],3:])