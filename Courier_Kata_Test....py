import unittest
from Courier_Kata_Heavy_Parcel import Parcel, Order

class ParcelTestCase(unittest.TestCase):
    def test_calculate_cost(self):
        # Create a heavy parcel with dimensions and weight
        parcel = Parcel([80, 80, 80], 12)
        
        order = Order()
        order.add_parcels(parcel)

        # Calculate the cost of the parcel
        total_cost = parcel.calculate_cost()
        
        # Verify that the calculated cost matches the expected cost
        expected_cost = 17  # Size cost + weight cost for extra weight
        
        self.assertEqual(total_cost, expected_cost)

if __name__ == '__main__':
    unittest.main()