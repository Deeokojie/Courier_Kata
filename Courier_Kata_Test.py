import unittest
from Courier_Kata import calculate_cost


class TestCourier(unittest.TestCase):
    def test_small_parcel_cost(self):
        dimensions = [1, 1, 1]

        result = calculate_cost(dimensions)

        expected = [
            {"type": "small parcel", "cost": 3},
            {"type": "small parcel", "cost": 3}
        ]
        self.assertEqual(result, expected)

        if __name__ == '__main__':
            unittest.main() 


            