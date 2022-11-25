import matplotlib.pyplot as plt
from waterdrop import WaterDrop

wd = WaterDrop()
wd.fill_trace()

# Set the size of plotting window.
plt.figure(dpi=85, figsize=(10.5,6.5))
plt.plot(wd.x_values, wd.y_values, linewidth=2, zorder=1)
# Emphasize start point and end point.
plt.scatter(0, 0, c='red', edgecolor='none', s=100, zorder=2)
plt.scatter(wd.x_values[-1], wd.y_values[-1], c='green',
edgecolor='none', s=100, zorder=2)

# # Set chart title and label axes.
# plt.title("Water Drops", fontsize=20)
# plt.xlabel("X values", fontsize=13)
# plt.ylabel("Y Values", fontsize=13)

# Remove the axes.
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
# Set tsize of tick labels.
plt.tick_params(axis='both', labelsize=10)
plt.show()
