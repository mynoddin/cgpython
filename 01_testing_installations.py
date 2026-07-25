import numpy as np
import matplotlib.pyplot as plt 

print("Numpy version:", np.__version__)
print("Matplotlib version:", plt.matplotlib.__version__)

x = [0,1,2,3] # x - axis values 
y = [0,1,4,9] # y - axis values


plt.plot(x,y) 
plt.title("Python Graphics Test") 
plt.show() 