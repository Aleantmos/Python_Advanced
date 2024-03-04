class Programmer:
    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned) -> str:
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed) -> str:
        if new_language == self.language:
            return f"{self.name} already know {new_language}"
        else:
            if self.skills >= skills_needed:
                self.language = new_language
                return f"{self.name} switched from {self.language} to {new_language}"
            else:
                needed_skills = skills_needed - self.skills
                return f"{self.name} needs {needed_skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
