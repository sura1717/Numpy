import numpy as np
a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
"""print(a)
print(b)
"""

#sort by an array   (it's return always array type)
print(np.sort(a))
print(np.sort(b))       #sortin in row wise 
print(np.sort(b,axis=0))        #sorting in column wise

##append a value
print(np.append(a,200))
print(np.append(b,np.ones(6)).reshape(6,5))

#concatinate same size of array
c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
#np.concatenate(c,d),axis=0             #not working

#find all unique values in array
e=np.array([1,3,2,4,2,3,2,1,5,6,5,3,6,3,6,2,6])
print(np.unique(e))

#extend dimentions in array
#print(np.expand_dims(a,axis=2))          not working

#where method return index according to conditions and replace it if i want it
print(b[np.where(b>50)])
#replace all greater then 50 values into 0
print(np.where(a[a%2==0]))          #somthing wrong in it

#return index of maximium and minimium value 
print(a)
print(np.argmax(a))
print(np.argmin(a))

#commulative sum and product of all array
print(np.cumsum(a))
print(np.cumprod(a))
print(np.cumsum(b,axis=0))      #sum in column wise in 2D array

#find percentile of an array
print(np.percentile(a,50))
print(np.percentile(b,100,axis=0))

#search multiple item in given array
items=[45,56,54,98,67,33,84]
print(np.isin(a,items))     #return a boolian list

#replace specific or  multiple values
print(np.put(a,[1,2],[110,220]))
print(a)

#flip or reverse whole array
print(np.flip(a))
print(b)
print(np.flip(b,axis=0))