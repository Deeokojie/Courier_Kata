class Order:
    # Initialiaze an order with an empty listof parcelsand no speedy shipping
    def __init__(self):
        self.parcels = []
        self.speedy_shipping = False

    def add_parcel(self, parcel):
        # Add a parcel to the order
        self.parcels.append(parcel)

    def calculate_total_cost(self):
        # Calculate the total cost of the order
        total_cost = sum(parcel.calculate_cost() for parcel in self.parcels)
        if self.speedy_shipping:
            total_cost *= 2
        return total_cost

    def get_invoice(self):
        # Create an invoice for the order
        invoice = []
        for i, parcel in enumerate(self.parcels, start =1):
            invoice.append(f"Parcel {i}: type: {parcel.__class__.__name__}, Cost: ${parcel.calculate_cost()}") 

        if self.speedy_shipping:
            speedy_shipping_cost = self.calculate_total_cost() // 2
            invoice.append(f"speedy Shipping: Cost: ${self.calculate_total_cost() // 2}")
        invoice.append(f"total Cost: ${self.calculate_total_cost()}")
        return "\n".join(invoice)





