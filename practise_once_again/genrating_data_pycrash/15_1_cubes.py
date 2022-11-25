import matplotlib.pyplot as plt
# cubes = [1, 8, 27, 64, 125]
# numbers = [1, 2 ,3 ,4, 5]
# numbers = [1, 2, 3, 4, 5]
# check_cubes = map(lambda x: x**3, numbers)
# print(list(check_cubes))
x_values = list(range(1, 500))
y_values = list(map(lambda x: x**3, x_values ))
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Greens,
            edgecolor='none', s=40)

# Set chat title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set range for the each axis.
plt.axis([0, 550, 0, 135000000])
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# plt.show()
plt.savefig('cubes_plot.png', bbox_inches='tight')
