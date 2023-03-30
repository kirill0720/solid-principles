"""
Animal, Dog, and Cat classes violate the Open-Closed Principle because they do not provide a common interface
for the make_sound() method. This means that if a new animal class is added in the future,
the AnimalSound class would need to be modified to include a new conditional statement.
"""


class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Bark bark!")


class Cat(Animal):
    def make_sound(self):
        print("Meow meow!")


class AnimalSound:
    def make_animal_sound(self, animal):
        animal.make_sound()


if __name__ == '__main__':
    sound_maker = AnimalSound()
    sound_maker.make_animal_sound(Dog())
    sound_maker.make_animal_sound(Cat())
