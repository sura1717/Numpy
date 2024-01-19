import numpy as np
a=np.array([1,3,4,3,5,np.nan,5,9,8])
print(np.isnan(a))
print(a[~(np.isnan(a))])

#filter all nan type value or missing value
