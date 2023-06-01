import math

class Parcel:
    def __init__(self, dimensions, weight):
        self.dimensions = dimensions
        self.weight = weight

    def calculate_cost(self):
        # Calculate the cost of the parcel based on its dimensions
        if all(dim < 10 for dim in self.dimensions):
            size_cost = 3

        elif all(dim < 50 for dim in self.dimensions):
                size_cost = 8

        elif all(dim < 100 for dim in self.dimensions):
            size_cost = 15

        else:
            size_cost = 25

        weight_limit = 0

        weight_cost= 0 

        # Determine weight limit and weight costbased on the size cost
        if size_cost == 3:
            weight_limit = 1
            weight_cost = 2

        elif size_cost == 8:
            weight_limit = 3
            weight_cost = 2

        elif size_cost == 15:
            weight_limit = 6
            weight_cost = 2

        elif size_cost == 25:
            weight_limit = 10
            weight_cost = 2        

        if self.weight > weight_limit:
            extra_weight = self.weight - weight_limit
            weight_cost *= extra_weight

            return size_cost + weight_cost





