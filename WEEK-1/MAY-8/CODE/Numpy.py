import numpy as np


fruits=np.array([['Apple','Banana','Orange'],
                ['Grapes','Kiwi','Lemon']])
print("The fruits are \n:",fruits)
print("The fruits in the first row are:",fruits[0]) #printing the first row
print("The shape is :",fruits.shape) #prints (rows,columns)
print("The size is :",fruits.size) #prints the total number of elements
print("The data type is :",fruits.dtype) #prints the data type of the elements in the array
print("The dimesion of the matrix is:",fruits.ndim) #prints the number of dimensions of the array

numbers=np.array([[1,6,3],
                  [8,5,2],
                  [7,4,9]])
print("The numbers are:\n",numbers)
print("The sum of the numbers is:",np.sum(numbers)) #sum of all the elements in the array
print("The mean of the numbers is:",np.mean(numbers)) #mean of all the elements in the array
print("The median of the numbers is:",np.median(numbers)) #median of all the elements in the array
print("The standard deviation of the numbers is:",np.std(numbers)) #standard deviation of all the elements in the array
print("The variance of the numbers is:",np.var(numbers)) #variance of all the elements in the array
print("The maximum of the numbers is:",np.max(numbers)) #maximum of all the elements in the array
print("The minimum of the numbers is:",np.min(numbers)) #minimum of all the elements in the array
print("The sorted numbers are:\n",np.sort(numbers)) #sorting the array in ascending order
print("The dot product of the numbers is:",np.dot(numbers,numbers)) #dot product of the array with itself
print("The cumulative sum of the numbers is:",np.cumsum(numbers)) #cumulative sum of the array
print("The cumulative product of the numbers is:",np.cumprod(numbers)) #cumulative product of the array

