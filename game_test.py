import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Initial coordinates of the point
x, y, z = 0, 0, 0

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the initial point
point, = ax.plot([x], [y], [z], 'ro')

# Set axis limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Update function to move the point
def update_point(event):
    global x, y, z

    # Check which key is pressed
    if event.key == 'up':
        y += 1
    elif event.key == 'down':
        y -= 1
    elif event.key == 'left':
        x -= 1
    elif event.key == 'right':
        x += 1
    elif event.key == 'w':  # Move in the positive z direction
        z += 1
    elif event.key == 's':  # Move in the negative z direction
        z -= 1

    # Update the point's position
    point.set_data([x], [y])
    point.set_3d_properties([z])
    
    # Redraw the figure
    fig.canvas.draw()

# Connect the update function to key press events
fig.canvas.mpl_connect('key_press_event', update_point)

# Show the plot
plt.show()
