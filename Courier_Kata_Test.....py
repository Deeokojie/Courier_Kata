import unittest
from Courier_Kata_Discount import Parcel, SmallParcel, MediumParcel, LargeParcel, XLParcel, HeavyParcel, Order

class OrderTestCase(unittest.TestCase):
    def test_calculate_total_cost(self):
        # Create the parcels for the order
        parcels = [
            SmallParcel([1, 1, 1], 1),
            SmallParcel([1, 1, 1], 1),
            SmallParcel([1, 1, 1], 1),
            SmallParcel([1, 1, 1], 1),
            MediumParcel([20, 20, 20], 2),
            MediumParcel([20, 20, 20], 2),
            MediumParcel([20, 20, 20], 2),
            LargeParcel([80, 80, 80], 5),
            XLParcel([110, 110, 110], 10),
            HeavyParcel([30, 30, 30], 60),
        ]

        # Create an order with the parcels
        order = Order(parcels)

        # Calculate the total cost of the order
        total_cost = order.calculate_total_cost()

        # Verify that the calculated total cost matches the expected total cost
        expected_total_cost = 94  # The expected total cost value
        self.assertEqual(total_cost, expected_total_cost)

if __name__ == '__main__':
    unittest.main()