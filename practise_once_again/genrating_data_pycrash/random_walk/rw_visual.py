import matplotlib.pyplot as plt
import pygal
from random_walk import RandomWalk

# Keep making new walks , as long as the program is active,
# while True:

# Make a random walk, and plot the points.
rw = RandomWalk(100)
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(dpi=80, figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    edgecolor='none', s=1)
# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
    s=100)

# Remove the axes.
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

# plt.show()
# Visualization with pygal.
pygal_chart = pygal.XY(stroke=False)
pygal_chart.title = 'Random Walk'
rwValues = list(zip(rw.x_values, rw.y_values))
pygal_chart.add('rw', rwValues)
pygal_chart.render_to_file('rw_visual.svg')
