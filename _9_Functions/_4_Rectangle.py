def rectangle(length, width):
    if not isinstance(length, int) and not isinstance(width, int):
        return "Enter valid values"

    def area():
        area_size = length * width
        return area_size

    def perimeter():
        perimeter_size = length * 2 + width * 2
        return perimeter_size

    result = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return result


print(rectangle(2, 10))
