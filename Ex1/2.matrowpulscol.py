#Create a 5×5 matrix whose every element is the sum of its row and column number

import numpy as np
a = np.zeros((5,5))
b=[]
for i in range(len(a)):
    t=[]
    for j in range(len(a[i])):
        t.append(i+j)
    b.append(t)
print(b)