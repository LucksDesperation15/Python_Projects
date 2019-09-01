# Product Inventory Project

# TODO: Have to seperate each constructor to its own
# property so it is able to update prod info

class Product(object):
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity
        self._test = 0

    @property
    def prod_info(self):
        self._prod_info = (self.price, self.id, self.quantity, self._test)
        return self._prod_info

    @prod_info.setter
    def prod_info(self, val):
        self._prod_info = val

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, val):
        self._test = val

# Just have to update the product info in the Inventory
# Would have to create method to look for apple and then
# update the values for apple. Perhaps a dic is better
# than a list for this purpose. Dic of tuples.

class Inventory(object):
    def __init__(self):
        self.productlist = []

    def add_product(self, products):
        self.products = products
        self.productlist.append(products.prod_info)

    def sum_of_products(self):
        self.product_sum =  sum([i[0] for i in self.productlist])
        return self.product_sum

    def __repr__(self):
        return str(self.sum_of_products())

apples = Product(1.00, 1234, 10)
oranges = Product(2.00, 4567, 10)
print(apples.price)
apples.test = 1234567
inventory = Inventory()
inventory.add_product(apples)
inventory.add_product(oranges)
print(inventory.productlist)
apples.test = 9435643
print(apples.prod_info)
print(inventory.productlist)
