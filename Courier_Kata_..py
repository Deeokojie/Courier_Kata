import math

class Parcel:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_volume(self):
        # Calculate the volume of the parcel by multiplying all dimensions
        return math.prod(self.dimensions)

class SmallParcel(Parcel):
    def __init__(self, dimensions, weight):
        super().__init__(dimensions)
        self.weight = weight
    
    def calculate_cost(self):
        # Calculate the cost of the small parcel based on its dimensions
        if all(dim < 10 for dim in self.dimensions):
            return 3
        else:
            return 8        

class MediumParcel(Parcel):
    def __init__(self, dimensions, weight):
        super().__init__(dimensions)
        self.weight = weight

    def calculate_cost(self):
        # Calculate the cost of the large parcel based on its dimensions
        if all(dim < 50 for dim in self.dimensions):
            return 8
        else:
            return 12     

class LargeParcel(Parcel):
     def __init__(self, dimensions, weight):
        super().__init__(dimensions)
        self.weight = weight

     def calculate_cost(self):
        # Calculate the cost of the large parcel based on its dimensions
        if all(dim < 100 for dim in self.dimensions):
            return 15
        else:
            return 18    

