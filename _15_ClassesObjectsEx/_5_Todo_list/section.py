from task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if self.tasks.__contains__(new_task):
            return f"Task is already in the section {new_task.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_cnt = 0
        new_task_list = []

        for task in self.tasks:
            if not task.completed:
                new_task_list.append(task)
            else:
                removed_cnt += 1

        self.tasks = new_task_list
        return f"Cleared {removed_cnt} tasks."

    def view_section(self):
        result = f"Section: {self.name}:\n"
        for task in self.tasks:
            result += task.details() + "\n"

        cleaned = result.strip()
        return cleaned


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

