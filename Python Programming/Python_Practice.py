#%%
a=int(input("Enter:"))
for i in range(a):
    print("*")
#%%
a=int(input("Enter a number:"))
l=[]
for i in range(a):
    k=input()
    l.append(k)
    print(l)
#%%
import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=np.log(x)
plt.plot(x,y)
#%%
import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[5,4,3,2,1]
plt.bar(x,y)
