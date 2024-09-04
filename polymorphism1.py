class Animal:
    def sound(self):
        print("Animal makes SOUND...")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Bird(Animal):
    def sound(self):
        print("Bids sing")
lion = Animal()
lion.sound()
Dog = Dog()
Dog.sound()
Bird = Bird()
Bird.sound()