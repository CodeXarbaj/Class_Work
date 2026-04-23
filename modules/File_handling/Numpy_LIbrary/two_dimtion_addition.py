#importing numpy library as np
import numpy as np 
#first array
array1 = np.array([90,50,40,70])
#second array
array2 = np.array([10,20,30,60])

#---------------------------------------
print(array1)
print("---------------------------------------")
print(array2)
print("----------------------------------------")

#sum of two array
arrayadd = np.add(array1,array2)
print(arrayadd)
print("-----------------------------------------------")

print("Substraction of two dimentional array")
arraysub = np.subtract(array1,array2)       #Using sunstract function for calculating diffrence of two array
print(arraysub)

print("---------------------------------------------------------")

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = A @ B                        #Using @ for matrix multiplication

print(result)
