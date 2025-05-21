#Why numpy
#Why id umpy faster ? Fixed type

#numpy ->>Int32
'''
Size ReferenceCount ObjectType,ObjectValue 

Faster to read less bytes of memory

'''

import numpy as np

a= np.array([1,2,3],dtype='int32')
#Get dimention
print(a,a.ndim)
#Multi dimentional array
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
#Get shape
print(b,b.shape)
#Get type
print(a.dtype)
#Get size
print(a.itemsize)
#Get total size
print(a.size)
print(a.nbytes)


'''
Accessing/Changing specific elements rows columns etc of the data
'''
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#Get a specific element [rowindex,columnindex]
#select 13
print(a[1,5])
#Get a specific row
print(a[0,:])
#Get a specific column
print(a[:,2])

#Getting little more fancy [Startindex:endindex:stepsize]
print(a[0,1:6:2])
print(a[0,1:-1:2])
a[1,5]=20
print(a)
a[:,2]=[1,2]
print(a)

#3D Array example

b= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Get specific element (work outside in)
print(b[0,1,1])
print(b[:,1,:])
print(b[:,0,:])
print(b[:,0,0])

#Replace
b[:,1,:] = [[9,9],[8,8]]
print(b)
