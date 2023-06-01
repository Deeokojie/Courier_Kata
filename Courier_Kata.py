import math 

class Parcel:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_volume(self):
        # Calculate the volume of the parcel by multiplying all 3 dimensions
        return math.prod(self.dimensions)

def calculate_cost(parcel):
    # Calculate the cost of the parcel by its dimensions
    volume = parcel.calculate_volume()
    
    #calculate small parcel cost
    if all(dim < 10 for dim in parcel.dimensions):
        return 3 
  
    #calculate meduim parcel cost
    elif all(dim < 50 for dim in parcel.dimensions):
        return 8    

    #calculate large parcel cost
    elif all(dim < 100 for dim in parcel.dimensions):
        return 15

    else:
        #calculate extra large cost
        return 25 


                    
