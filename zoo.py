# Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Animal():
    def __init__(self, name, age, attribute):
        self.name = name
        self.age = age
        self.attribute = attribute

    def make_sound(self):
        pass
    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, attribute):
        super().__init__(name, age, attribute)

    def make_sound(self):
        print(self.attribute, self.name, "поет")

    def eat(self):
        print(self.attribute, self.name, "клюет зерна")


class Mammal(Animal):
    def __init__(self, name, age, attribute):
        super().__init__(name, age, attribute)

    def make_sound(self):
        print(self.attribute, self.name, "трубит")

    def eat(self):
        print(self.attribute, self.name, "ест траву")


class Reptile(Animal):
    def __init__(self, name, age, attribute):
        super().__init__(name, age, attribute)

    def make_sound(self):
        print(self.attribute, self.name, "шипит")

    def eat(self):
        print(self.attribute, self.name, "ест кроликов")


class ZooKeeper():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.job = "смотритель"

    def feed_animal(self):
        print(self.name, "кормит животных")


class Veterinarian():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.job = "ветеринар"

    def heal_animal(self):
        print(self.name, "лечит животных")


class Zoo():
    def __init__(self, zoo_name, address):
        self.zoo_name = zoo_name
        self.address = address
        self.zoo_animals = []
        self.zoo_workers = []

    def add_animals(self, animal):
        self.zoo_animals.append(animal)
        print("В список добавлено животное:", animal.attribute, animal.name, animal.age, "лет")

    def show_animals(self):
        if self.zoo_animals:
            print("Список животных:")
            for animal in self.zoo_animals:
                print("животное:", animal.attribute, animal.name, animal.age, "лет")
        else:
            print("В списке нет животных")

    def add_worker(self, worker):
        self.zoo_workers.append(worker)
        print("В штатное расписание добавлен сотрудник:  ID -", worker.id, ",  имя:", worker.name, ",  должность:", worker.job)

    def show_workers(self):
        if self.zoo_workers:
            print("Список сотрудников:")
            for worker in self.zoo_workers:
                print(" ID -",  worker.id, ",  должность -", worker.job, ",  имя:", worker.name)
        else:
            print("В списке нет сотрудников")


zoo = Zoo("Ленинградский зоопарк", "Кронверкский пр., 4")
bird = Bird("канарейка", "5", "Желтая")
zoo.add_animals(bird)
worker = Veterinarian("v1", "Иван")
zoo.add_worker(worker)
zoo.show_workers()
zoo.show_animals()
