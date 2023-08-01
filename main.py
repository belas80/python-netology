class Animals:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f'Покормили {self.name}')


class Gooses(Animals):

    def gather_eggs(self):
        print(f'Собираем яйца у {self.name}')


class Cows:
    name = ''
    weight = 0


class Sheep:
    name = ''
    weight = 0


class Chickens:
    name = ''
    weight = 0


class Goats:
    name = ''
    weight = 0


class Ducks:
    name = ''
    weight = 0


if __name__ == '__main__':
    goose_1 = Gooses('Серый', '1')
    goose_1.gather_eggs()
    goose_1.feed()
    goose_2 = Gooses(name='Белый', weight='2')
    print(f'Вес у гуся {goose_2.name} - {goose_2.weight}')
    goose_2.feed()
