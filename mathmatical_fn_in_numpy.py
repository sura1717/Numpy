import numpy as np
def sigmoid(arr):
    return 1/1+np.exp(-(arr))

def MSE(arr1,arr2):
    return np.mean((arr1-arr2)**2)
"""def BCE(arr1,arr2):
    return np.mean(-((arr2*(np.log(1-arr1)))+(1-arr2)*(np.log(1-arr1))))"""
a=np.random.randint(1,50,20)
b=np.random.randint(1,50,20)
print("sigmoid of whole array a is ",sigmoid(a))
#print(BCE(a,b))          this function are not working formula is wrong
print()
print("sigmoid of whole array b is ",sigmoid(b))
print()
print("the mean square error of two array is ",MSE(a,b))