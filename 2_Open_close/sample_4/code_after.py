"""
The solution is to create an abstract Animal class that defines the make_sound() method as abstract.
The Dog and Cat classes then inherit from the Animal class and implement the make_sound() method.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
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
