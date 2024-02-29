def operate(command, *args):
    def add():
        result = 0
        for el in args:
            result += el
        return result

    def subtract():
        result = 0
        for el in args:
            result -= el
        return result

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def divide():
        result = 1
        for el in args:
            if el != 0:
                result /= el
            else:
                return "Operation not valid"
        return result

    if command == "+":
        return add()
    elif command == "-":
        return subtract()
    elif command == "*":
        return multiply()
    elif command == "/":
        return divide()


print(operate("+", 1, 2, 3))

