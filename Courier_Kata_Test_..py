import unittest

from Courier_Kata_2 import SmallParcel, MediumParcel, LargeParcel 
from Courier_Kata_Order import Order



class OrderTestCase(unittest.TestCase):
    def test_get_invoice(self):
        order = Order()
        order.speedy_shipping = True

        small_parcel = SmallParcel([1, 1, 1], 1)
        medium_parcel = MediumParcel([20, 20, 20], 2)
        large_parcel = LargeParcel([80, 80, 80], 5)
        
        order.add_parcel(small_parcel)
        order.add_parcel(medium_parcel)
        order.add_parcel(large_parcel)
        
        expected_invoice = "Parcel 1: type: SmallParcel, Cost: $3\n" \
                           "Parcel 2: type: MediumParcel, Cost: $8\n" \
                           "Parcel 3: type: LargeParcel, Cost: $15\n" \
                           "speedy Shipping: Cost: $26\n" \
                           "total Cost: $52"
        
        invoice = order.get_invoice()
        self.assertEqual(invoice, expected_invoice)

if __name__ == '__main__':
    unittest.main()