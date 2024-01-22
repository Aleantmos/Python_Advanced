timeline = 0


def read_robots_data():
    robots_data = {}
    elements = input().split(";")

    for i in range(len(elements)):
        tokens = elements[i].split("-")
        robot_name = tokens[0]
        capacity = int(tokens[1])
        robots_data[robot_name] = capacity

    return robots_data


def convert_into_seconds(timeline_str):
    timeline = 0
    tokens = timeline_str.split(":")

    hours = int(tokens[0])
    hours_in_seconds = hours * 60 * 60
    timeline += hours_in_seconds

    minutes = int(tokens[1])
    minutes_in_seconds = minutes * 60
    timeline += minutes_in_seconds

    seconds = int(tokens[2])
    timeline += seconds

    return timeline


def read_timeline_start():
    timeline_str = input()
    return convert_into_seconds(timeline_str)


def read_initial_data():
    robots = read_robots_data()
    timeline_start = read_timeline_start()
    return robots, timeline_start


def set_initial_available_robots(robots):
    robots_unavailability = {}
    for robot_name in robots.keys():
        robots_unavailability[robot_name] = 0

    return robots_unavailability


def get_next_available_robot(timeline, unavailability):
    for key, value in unavailability.items():
        if timeline > value:
            return key

    return None


def convert_into_time(timeline):
    hour_factor = 3600
    hours = timeline // hour_factor
    rest = timeline % hour_factor

    minutes_factor = 60
    minutes = rest // minutes_factor
    seconds = rest % minutes_factor

    result = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return result


def assign_task_to_available(task, available, timeline, robots, robots_unavailability):
    capacity = robots.get(available)
    deadline = timeline + capacity
    robots_unavailability[available] = deadline

    time = convert_into_time(timeline)
    print(f"{available} - {task} [{time}]")


def do_process_flow(robots, timeline):
    robots_unavailability = set_initial_available_robots(robots)
    tasks = []
    task = ""
    all_tasks_read = False

    while not all_tasks_read or len(tasks) != 0:
        timeline += 1
        available = get_next_available_robot(timeline, robots_unavailability)
        all_tasks_read, task = read_task(all_tasks_read, task)

        if not all_tasks_read:
            if available is not None:
                assign_task_to_available(task=task,
                                         available=available,
                                         timeline=timeline,
                                         robots=robots,
                                         robots_unavailability=robots_unavailability)
            else:
                tasks.append(task)
        else:
            if available is not None:
                task = tasks.pop(0)
                assign_task_to_available(task=task,
                                         available=available,
                                         timeline=timeline,
                                         robots=robots,
                                         robots_unavailability=robots_unavailability)


def read_task(all_tasks_read, task):
    if not all_tasks_read:
        task = input()
        if task == "End":
            all_tasks_read = True

    return all_tasks_read, task


def start():
    robots, unavailability_plan = read_initial_data()
    do_process_flow(robots, unavailability_plan)


start()
