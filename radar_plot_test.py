import numpy as np
import matplotlib.pyplot as plt

dist = np.array([2,2,3,4,5])
angle = np.array([np.deg2rad(0),np.deg2rad(45),np.deg2rad(90),np.deg2rad(135),np.deg2rad(270)])
height = np.array([1,2,3,4,5])

fig, ax1 = plt.subplots(subplot_kw={'projection': 'polar'})
ax1.scatter(angle, dist)
ax1.set_rmax(2)
ax1.set_rticks([1, 2, 3, 4,5,6])  # Less radial ticks
ax1.set_rlabel_position(0)  # Move radial labels away from plotted line
ax1.grid(True)

ax1.set_title("Radar data on polar plot", va='bottom')
plt.show()