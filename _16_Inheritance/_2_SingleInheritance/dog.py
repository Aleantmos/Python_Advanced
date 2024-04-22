from _2_SingleInheritance.animal import Animal


class Dog(Animal):
    def bark(self):
        super()
        return "barking..."
