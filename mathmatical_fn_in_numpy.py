import numpy as np
def sigmoid(arr):
    return 1/1+np.exp(-(arr))

def MSE(arr1,arr2):
    return np.mean((arr1-arr2)**2)

a=np.random.randint(1,50,20)
b=np.random.randint(1,50,20)
print("sigmoid of whole array a is ",sigmoid(a))
print()
print("sigmoid of whole array b is ",sigmoid(b))
print()
print("the mean square error of two array is ",MSE(a,b))