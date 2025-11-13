class Animal: #Сам класс
    def __init__(self, num_paws: int, voice: bool, self_sound: str) -> None:
        self.num_paws = num_paws
        self.voice = voice
        self.self_sound = self_sound

    #Метод
    def make_sound(self):
        if self.voice:
            print("Говорящее животное")
        else:
            print("Неговорящее животное")


class Dog(Animal):
    def __init__(self, name:str, color:str) -> None:
        self.num_paws = 4
        self.voice = True
        self.self_sound = "Gav"
        self.name = name
        self.color = color

dog = Dog(name="Шарик", color="Коричневый")


class Cat(Animal):
    def __init__(self, name:str, color:str) -> None:
        self.num_paws = 4
        self.voice = True
        self.self_sound = "Meow"
        self.name = name
        self.color = color

cat = Cat(name="Машка", color="Черный")


class Fish(Animal):
    def __init__(self, name:str, color:str) -> None:
        self.num_paws = 0
        self.voice = False
        self.self_sound = None
        self.name = name
        self.color = color

fish = Fish(name="Васёк", color="Голубой")

class Bird(Animal):
    def __init__(self, name:str, can_fly:bool) -> None:
        self.num_paws = 0
        self.voice = True
        self.self_sound = "Чик-чирик"
        self.name = name
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print("Летает")
        else:
            print("Не летает")


bird = Bird(name="Синица", can_fly=True)


bird.fly()


dog.make_sound()
cat.make_sound()
fish.make_sound()


print(dog.self_sound)
print(cat.name)