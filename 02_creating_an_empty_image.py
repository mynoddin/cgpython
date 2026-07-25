import numpy as np 
import matplotlib.pyplot as plt 

height = 300
width = 400 

image = np.zeros((height, width, 3), dtype=np.uint8) 

plt.imshow(image,cmap='gray') # display the image using matplotlib 
plt.axis("off") # turn off axis labels 
plt.show() # show the image