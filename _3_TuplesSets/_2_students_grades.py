def read_data():
    students = {}
    count = int(input())
    for i in range(count):
        line = input().split(" ")
        key = line[0]
        value = float(line[1])
        if key in students.keys():
            students[key].append(value)
        else:
            students[key] = [float(line[1])]

    return students


def calculate_average_for_each(students):
    averages = {}
    for key, values in students.items():
        total = 0
        for value in values:
            total += value

        current_average = total / len(values)
        averages[key] = current_average

    return averages


def print_result(students, averages):
    for name in students.keys():
        grades_str = " ".join(('{:.2f}'.format(grade) for grade in students.get(name)))
        average_str = ("(avg: {:.2f})".format(averages.get(name)))
        result = name + " -> " + grades_str + " " + average_str
        print(result)


def start():
    # read and lines and collect in dictionary
    students = read_data()

    # calculate and collect average in name:average pair
    averages = calculate_average_for_each(students)

    print_result(students, averages)


start()
