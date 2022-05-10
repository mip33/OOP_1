class Animals:
    def __init__(self, name, sound, weight):
        self.name = name
        self.sound = sound
        self.weight = weight

    def eat(self):
        print('Покормили {}'.format(self.name))


class AnimalsWithEggs(Animals):
    def eggs(self):
        print('Собрали яйца y {}'.format(self.name))


class AnimalsWithMilk(Animals):
    def milk(self):
        print('Подоили {}'.format(self.name))


class Goose(AnimalsWithEggs):
    def __str__(self):
        return 'Гуся зовут: {}, издаваемый звук: "{}", вес: {}'.format(self.name, self.sound, self.weight)


class Cow(AnimalsWithMilk):
    def __str__(self):
        return 'Корову зовут: {}, издаваемый звук: "{}", вес: {}'.format(self.name, self.sound, self.weight)


class Sheep(Animals):
    def cut(self):
        print('Подстригли {}'.format(self.name))

    def __str__(self):
        return 'Овцу зовут: {}, издаваемый звук: "{}", вес: {}'.format(self.name, self.sound, self.weight)


class Chicken(AnimalsWithEggs):
    def __str__(self):
        return 'Курочку зовут: {}, издаваемый звук: "{}", вес: {}'.format(self.name, self.sound, self.weight)


class Goat(AnimalsWithMilk):
    def __str__(self):
        return 'Козу зовут: {}, издаваемый звук: "{}", вес: {}'.format(self.name, self.sound, self.weight)


class Duck(AnimalsWithEggs):
    def __str__(self):
        return 'Утку зовут: {}, издаваемый звук: "{}", вес: {}'.format(self.name, self.sound, self.weight)


cow = Cow('Манька', 'My-My', 650)  # Корова
print(cow)
cow.eat()
cow.milk()

print()

goose_1 = Goose('Серый', 'кря-кря', 3)  # 2 Гуся
goose_2 = Goose('Белый', 'кря-кря', 4)
print(goose_1, goose_2, sep="\n")
goose_1.eat()
goose_1.eggs()
goose_2.eggs()

print()

sheep_1 = Sheep('Барашек', 'Меееее-мееее', 150)  # 2 Овцы
sheep_2 = Sheep('Кудрявый', 'Меееее-Мееее', 120)
sheep_1.eat()
sheep_2.eat()
sheep_2.cut()
sheep_1.cut()
print(sheep_1, sheep_2, sep="\n")

print()

chicken_1 = Chicken('Ко-Ко', 'кудах-кудах', 2)  # 2 Курицы
chicken_2 = Chicken('Кукареку', 'кудах-кудах', 3)
chicken_1.eat()
chicken_2.eat()
chicken_1.eggs()
chicken_2.eggs()
print(chicken_1, chicken_2, sep="\n")

print()

goat_1 = Goat('Рога', 'Беееее-бееее', 30)  # 2 Kozi
goat_2 = Goat('Копыта', 'Беееее-бееее', 27)
goat_2.eat()
goat_1.eat()
goat_1.milk()
goat_2.milk()
print(goat_1, goat_2, sep='\n')

print()

duck = Duck('Кряква', 'кря-кря', 2)
duck.eggs()
duck.eat()
print(duck)

temp = None
list_animals = {
    'duck': 2,
     'goat_1': 3, 'goat_2': 4,
     'sheep_2': 120, 'sheep_1': 150,
     'goose_2': 4, 'goose_1': 3,
     'chicken_2': 3, 'chicken_1': 1,
     'cow': 650}

temp = None
total = 0
count = 0
for key,val in list_animals.items():
    if total <= val:
        count = val
        total += val
        temp = key



print(f'Общий вес животныж: {total}')
print(f'{temp} самое тяжелое животное, с весом {count}')
