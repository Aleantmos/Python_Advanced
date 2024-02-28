def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda item: (-sum(item[1]), item[0]))

    result = []

    for cheese, quantities in sorted_cheeses:
        print(f"{cheese}")
        sorted_quantities = sorted(quantities, reverse=True)
        for el in sorted_quantities:
            print(el)

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
