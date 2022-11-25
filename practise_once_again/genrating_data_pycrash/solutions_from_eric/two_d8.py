from  plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D8 dice.

die_1 = Die(num_sides=8)
die_2 = Die(num_sides=8)

# Make some  rolls, and store results in a list.
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequancies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result):
    frequency = results.count(value)
    frequancies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequancies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequance of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1,000,000',
    xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout':  my_layout}, filename='d8_d8.html')
