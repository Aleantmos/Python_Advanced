def read_data():
    symbols = [symbol for symbol in input()]
    return symbols


def count_symbols_sorted(symbols):
    counter = {}
    for symbol in symbols:
        result = counter.get(symbol)
        if result is not None:
            result += 1

        counter[symbol] = 1

    sorted_counter = dict(sorted(counter.items()))

    return sorted_counter


def print_result(result):
    for symbol, count in result.items():
        print(f"{symbol} : {count} time/s ")


def start():
    symbols = read_data()

    result = count_symbols_sorted(symbols)

    print_result(result)


start()
