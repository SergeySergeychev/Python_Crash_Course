from random import choice
import matplotlib.pyplot as plt

class WaterDrop():
    """A Class to present a drop of a water on surface."""
    def __init__(self, num_points=5000):
        # Initialize attributes of water drop.
        self.num_points = num_points
        # All leakage
        self.x_values = [0]
        self.y_values = [0]

    def fill_trace(self):
        # Keep filling trace untile it reaches desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go.
            x_direction = choice([-1, 1])
            x_dropes = choice([0, 1, 2, 3, 4])
            x_path = x_direction * x_dropes

            y_direction = choice([-1, 1])
            y_dropes = choice([0, 1, 2, 3, 4])
            y_path = y_direction * y_dropes

            # Keep leakage if no dropes are coming.
            if x_path and y_path == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_path
            next_y = self.y_values[-1] + y_path
            

            self.x_values.append(next_x)
            self.y_values.append(next_y)
