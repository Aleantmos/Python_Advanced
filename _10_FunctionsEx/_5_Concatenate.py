def concatenate_args(args):
    return "".join(args)


def replace_element(k, v, args_list):
    for i, el in enumerate(args_list):
        if el == k:
            args_list[i] = v


def concatenate(*args, **kwargs):
    args_list = list(args)

    for k, v in kwargs.items():
        replace_element(k, v, args_list)

    return "".join(args_list)


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
