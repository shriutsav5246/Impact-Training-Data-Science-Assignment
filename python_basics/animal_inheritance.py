def animal_info_decorator(func):
    def wrapper(*args, **kwargs):
        print("----- Animal Action -----")
        func(*args, **kwargs)
        print("-------------------------")
    return wrapper


class Animal:
    def __init__(self, name):
        self.name = name

    @animal_info_decorator
    def eat(self):
        print(f"{self.name} is eating.")

    @animal_info_decorator
    def drink(self):
        print(f"{self.name} is drinking.")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Bark!")


# Main execution
cat = Cat("Kitty")
dog = Dog("Tommy")

cat.eat()
cat.drink()
cat.sound()

print()

dog.eat()
dog.drink()
dog.sound()