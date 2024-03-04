class Pokemon:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def pokemon_details(self) -> str:
        return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = list()

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if self.pokemons.__contains__(pokemon):
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, name: str):
        searched = ""
        for el in self.pokemons:
            if el.name == name:
                searched = el
                break

        if searched == "":
            return "Pokemon is not caught"
        else:
            self.pokemons.remove(searched)
            return f"You have released {searched.name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

