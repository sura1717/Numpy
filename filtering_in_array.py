# for filtering in array
import numpy as np

#that is called boolean indexing or boolean filtering
suraj=np.random.randint(1,100,24).reshape(6,4)
print(suraj)
print(suraj[suraj>50])                      #all numbers value is true where value is greaterthen 12 and print that values
print(suraj[(suraj>50) & (suraj%7 !=0)])  #here both condition is occupy

#this is called fency indexing
suraj2=np.arange(24).reshape(6,4)
print(suraj2)
print(suraj2[[1,3]])        #here we are printing 1st and third rows
print(suraj2[:,[1,3]])#here we are print 1st and 3rd column

#now we are trying to print 1st and 3rd column and 4th and 5th rows
print(suraj2[[3,4],[0,1]])


