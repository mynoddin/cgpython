import numpy as np 
import matplotlib.pyplot as plt 

image = np.zeros((300, 400, 3), dtype=np.uint8)

image[100,100] = [255, 0, 0] # red pixel
image[101,100] = [0, 255, 0] # green pixel
image[100, 101] = [255,0,0] # red pixel

plt.imshow(image) 
plt.show() 
