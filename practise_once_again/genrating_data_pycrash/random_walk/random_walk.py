from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        

    def get_step(self):
        """Function to calculate steps"""
        random_direction = choice([1, -1])
        random_distance = choice([0, 1, 2, 3, 4])
        number_of_step = random_direction * random_distance
        return number_of_step

    def fill_walk(self):
        #  Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in tht dir.
            random_direction = choice([1, -1])
            random_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])


            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values._of
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
