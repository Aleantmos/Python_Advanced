def grocery_store(**kwargs):
    sorted_products = sorted(kwargs.items(),
                             key=lambda item: (-item[1], -len(item[0]), item[0]))
    receipt_lines = [f"{product}: {quantity}" for product, quantity in sorted_products]

    receipt = "\n".join(receipt_lines)

    return receipt


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
