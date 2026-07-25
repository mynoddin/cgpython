import numpy as np 
import matplotlib.pyplot as plt 

height = 300
width = 400 

image = np.zeros((height, width, 3), dtype=np.uint8) 

image[:, :] = [255, 255, 255] 


plt.imshow(image) # display the image using matplotlib 
plt.axis("on") # turn off axis labels 
plt.show() # show the image
