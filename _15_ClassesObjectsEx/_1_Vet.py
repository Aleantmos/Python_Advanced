class Vet:
    animals = []
    space = 5

    def __init__(self, name: str, ):
        self.name = name
        self.animals_cnt = 0

    def register_animal(self, animal_name):
        if len(Vet.animals) + 1 <= Vet.space:
            Vet.animals.append(animal_name)
            self.animals_cnt += 1
            return f"{animal_name} registered in the clinic"

        return "Not enough space"

    def unregister_animal(self, animal_name):
        try:
            Vet.animals.remove(animal_name)
            self.animals_cnt -= 1
            return f"{animal_name} unregistered successfully"
        except ValueError as e:
            return f"{animal_name} not in the clinic"

    def info(self):
        space_left_in_clinic = Vet.space - len(Vet.animals)
        return f"{self.name} has {self.animals_cnt} animals. {space_left_in_clinic} space left in clinic"



peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())

