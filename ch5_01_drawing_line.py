import matplotlib.pyplot as plt

x1, y1 = 1, 1
x2, y2 = 8, 6

plt.plot([x1,x2], [y1,y2]) 
plt.scatter([x1,x2], [y1,y2])

plt.grid(True)
plt.axis("equal") 
plt.show()