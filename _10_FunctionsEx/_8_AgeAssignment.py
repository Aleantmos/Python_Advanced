def get_first_letter(name_container):
    letters = {}

    for v in name_container:
        letters[v[0]] = v

    return letters


def age_assignment(*args, **kwargs):
    name_age_dict = {}

    name_container = list(args)
    letter_container = get_first_letter(name_container)

    for k, v in kwargs.items():
        name = letter_container.get(k)
        if name != "":
            name_age_dict[name] = f"{name} is {v} years old."

    name_age_dict_sorted = {k: name_age_dict[k] for k in sorted(name_age_dict)}

    return "\n".join(name_age_dict_sorted.values())


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
