class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f'Покормили {self.name}')


class Bird:

    def get_eggs(self):
        print(f'Собрали яйца')


class Milk:

    def get_milk(self):
        print(f'Подоили')


class Goose(Animal, Bird):

    type_animal = 'гусь'

    def say(self):
        print('Га Га Га')


class Cow(Animal, Milk):

    type_animal = 'корова'

    def say(self):
        print('Муууу')


class Sheep(Animal):

    type_animal = 'овца'

    def say(self):
        print('Беее')

    def cut(self):
        print(f'Подстригли {self.type_animal} {self.name}')


class Chicken(Animal, Bird):

    type_animal = 'курица'
    def say(self):
        print('Ко Ко Ко')


class Goat(Animal, Milk):

    type_animal = 'коза'

    def say(self):
        print('Мееее')


class Duck(Animal, Bird):

    type_animal = 'утка'

    def say(self):
        print('Кря Кря Кря')


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
