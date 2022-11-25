from die import Die
import pygal
import matplotlib.pyplot as plt

# Create a D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()
# Make some rolls, and store results in a list.
results = [die_1.roll() * die_2.roll() for roll in range(1000)]
# print(sorted(set(results)))

# Analyze the results.
x_labels_list = sorted(list(set((i*j) for i in range(1, 7) for j in range(1, 7))))
frequancies= [results.count(x) for x in x_labels_list]
# print(frequancies)

# Visualize the results.
hist = pygal.Bar()

hist.title ="Results of rolling two D6 dice and multiply them 1000 times."
hist.x_labels = x_labels_list
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequancies)
hist.render_to_file('die_visual.svg')
str_x_labels_list = [str(x) for x in x_labels_list]
# Bar plot with matplotlib.
plt.bar(str_x_labels_list, frequancies, width=0.8, edgecolor='black')
# Set chart title and label axes
plt.title("Die Roll D6 * D6", fontsize=20)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.show()
