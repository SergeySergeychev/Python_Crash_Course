from matplotlib import pyplot as plt

# Define data.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# Make plot.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes,
    cmap=plt.cm.Greens, s=10)

# Set char title and label axis.
ax.set_title("Cubes", fontsize=24)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.set_xlabel("Value", fontsize=14)

# Set size tick  labels, and set range for each axis.
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])
# plt.xlim(0, 5100)
# plt.ylim(0, 5100**3)

# SHow plot.
plt.show()
