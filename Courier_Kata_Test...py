import unittest
from Courier_Kata_complaint_solution import Parcel

class ParcelTestCase(unittest.TestCase):
    def test_calculate_cost(self):
        # Create a parcel with dimensions [5, 5, 5] and weight 2
        parcel = Parcel([5, 5, 5], 2)
        
        # Calculate the cost of the parcel
        cost = parcel.calculate_cost()
        
        # Verify that the calculated cost matches the expected cost
        expected_cost = 5
        self.assertEqual(cost, expected_cost)

if __name__ == '__main__':
    unittest.main()