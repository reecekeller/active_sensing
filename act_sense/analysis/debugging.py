import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
BASE_PATH = "/Users/reecekeller/Documents/Xaq/act_sense/act_sense/data/"

# Define the size of the heatmap
info_map = np.load(BASE_PATH + 'info_matrix.npy')
rows, cols = info_map.shape

# Create a grid of x and y coordinates
x = np.linspace(0, cols, cols)
y = np.linspace(0, rows, rows)
x, y = np.meshgrid(x, y)


info_d = info_map # change to desired fourth dimension
minn, maxx = info_d.min(), info_d.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='viridis')
m.set_array([])
fcolors = m.to_rgba(info_d)

# Plot the heatmap in the XY plane (Z = 0)
ax.plot_surface(x, y, np.zeros_like(info_map), facecolors=fcolors)

# Adjust labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim(0, 1)

# Show plot
plt.show()