class Product(object):
    def _init_(self, name, price):
        self.name = name
        self.price = price

class Cart(object):
    def __init__(self):
        self.product = []        

    def addProduct(self, product):
        self.product.append(product)

cart = Cart()
cart.addProduct(Product("Orange", "4.99"))
cart.addProduct(Product("Apple", "3.99"))

subTotal = ()
print “subtotal = $” +str(subTotal)

salesTax = subtotal * 0.06
print “sales tax = $” +str(salesTax)

totalAmount = (subTotal + salesTax)

print “Total = $” +str(totalAmount)

