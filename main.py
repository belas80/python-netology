class Animals:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f'Покормили {self.name}')


class Gooses:
    name = ''
    weight = 0


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
    my_cow_1 = Animals()
    my_cow_1.type = Cows()
    my_cow_1.type.name = 'Манька'
    my_goose_1 = Gooses()
    my_goose_1.name = 'Серый'
    print(my_goose_1.name)
    print(my_cow_1.type.name)

