def read_data():
    symbols = list(input())
    return symbols


def check_opening(symbol):
    return symbol == "{" or symbol == "[" or symbol == "("


def check_closing(symbol):
    return symbol == "}" or symbol == "]" or symbol == ")"


def check_parentheses(open, close):
    if open == "(" and close == ")":
        return True
    elif open == "{" and close == "}":
        return True
    elif open == "[" and close == "]":
        return True
    else:
        return False


def check_balance(data):
    isBalanced = True
    balance_stack = []
    for symbol in data:
        if check_opening(symbol):
            balance_stack.append(symbol)
        elif check_closing(symbol):
            opened = balance_stack.pop()
            closing = symbol
            result = check_parentheses(opened, closing)
            if not result:
                isBalanced = False

        if not isBalanced:
            return isBalanced

    return isBalanced


def start():
    data = read_data()
    result = check_balance(data)
    print(result)


start()
