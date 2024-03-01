def fill_the_box(*args):
    b_variables = args[:3]
    cubes = args[3:]
    b_volume = b_variables[0] * b_variables[1] * b_variables[2]

    negative_sum = 0

    for el in cubes:
        if el == "Finish":
            break
        b_volume -= el

        if b_volume < 0:
            negative_sum += el
            b_volume = 0

    if negative_sum == 0:
        return f"There is free space in the box. You could put {b_volume} more cubes."
    else:
        return f"No more free space! You have {negative_sum} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
