class Animal:

    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f'Покормили {self.name}')

    def say(self):
        print(self.voice)


class Bird(Animal):

    def get_eggs(self):
        print(f'Собрали яйца у {self.name}')


class Milk(Animal):

    def get_milk(self):
        print(f'Подоили')


class Goose(Bird):

    type_animal = 'гусь'
    voice = 'Га Га Га'


class Cow(Milk):

    type_animal = 'корова'
    voice = 'Муууу'


class Sheep(Animal):

    type_animal = 'овца'
    voice = 'Беее'

    def cut(self):
        print(f'Подстригли {self.type_animal} {self.name}')


class Chicken(Bird):

    type_animal = 'курица'
    voice = 'Ко Ко Ко'


class Goat(Milk):

    type_animal = 'коза'
    voice = 'Мееее'


class Duck(Bird):

    type_animal = 'утка'
    voice = 'Кря Кря Кря'


if __name__ == '__main__':
    goose_1 = Goose('Серый', 1)
    goose_2 = Goose(name='Белый', weight=2)
    cow_1 = Cow(name='Манька', weight=15)
    sheep_1 = Sheep('Барашек', 5)
    sheep_2 = Sheep('Кудрявый', 4)
    chicken_1 = Chicken('Ко-Ко', 1)
    chicken_2 = Chicken('Кукареку', 1)
    goat_1 = Goat('Рога', 7)
    goat_2 = Goat('Копыта', 8)
    duck_1 = Duck('Кряква', 3)

    list_animals = [goose_1, goose_2, cow_1, sheep_1, sheep_2,
                    chicken_1, chicken_2, goat_1, goat_2, duck_1]

    sum_weight = 0
    max_weight = 0
    max_animal = ''

    for i in list_animals:
        sum_weight += i.weight
        if i.weight > max_weight:
            max_weight = i.weight
            max_animal = i

    print(f'Общий вес животных - {sum_weight}')
    print(f'Самое тяжелое животное - {max_animal.type_animal} {max_animal.name}')
    chicken_1.say()
