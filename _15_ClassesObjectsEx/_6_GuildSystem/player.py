class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        curr_skill = self.skills.get(skill_name)
        if curr_skill is None:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        res = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"

        for skill_name, mana_cost in self.skills.items():
            res += f"==={skill_name} - {mana_cost}\n"

        cleaned = res.strip()
        return cleaned
