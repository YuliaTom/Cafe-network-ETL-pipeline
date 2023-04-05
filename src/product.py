
# Creating product class

class Product:
    def __init__(self, name, price, size, flavour=None):
        self.name = name
        self.price = price
        self.size = size
        self.flavour = flavour

# Allows to print content of the object

    def __str__(self):
        return (self.name, self.price)

    def __repr__(self):
        return "<Name:%s Size:%s Flavour:%s Price:%s>" % (self.name, self.size, self.flavour, self.price)

# Hashing method(s)  Compare hashes and keep unique values

    def __hash__(self) -> int:
        return hash((self.name, self.size, self.flavour, self.price))

# Makes sure no duplications in hashing

    def __eq__(self, other):
        return other and self.name == other.name and self.size == other.size and self.flavour == other.flavour and self.price == other.price
