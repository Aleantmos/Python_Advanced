from Product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        product = self.find(product_name)

        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        output = ""
        for product in self.products:
            output += f"{product.name}: {product.quantity}\n"
        return output
