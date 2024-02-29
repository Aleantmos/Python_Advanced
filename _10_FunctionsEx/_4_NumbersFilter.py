def even_odd_filter(**kwargs):
    filtered_dict = {}

    for key, numbers in kwargs.items():

        filtered_numbers = []

        if key == "even":
            for num in numbers:
                if num % 2 == 0:
                    filtered_numbers.append(num)
        elif key == "odd":
            for num in numbers:
                if num % 2 == 1:
                    filtered_numbers.append(num)

        filtered_dict[key] = filtered_numbers

    sorted_keys = sorted(filtered_dict, key=lambda key: len(filtered_dict[key]), reverse=True)
    sorted_dict = {key: filtered_dict[key] for key in sorted_keys}

    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
