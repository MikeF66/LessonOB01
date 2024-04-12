from abc import ABC, abstractmethod
from random import choice

class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter):
        pass

class Sword(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self, fighter):
        print(f'{fighter.name} наносит удар мечом')

class Axe(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self, fighter):
        print(f'{fighter.name} наносит удар топором')

class Bow(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self, fighter):
        print(f'{fighter.name} стреляет из лука')

class Halberd(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self, fighter):
        print(f'{fighter.name} наносит удар алебардой')


class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon
        print(f'{self.name} выбирает {new_weapon.name}')


class Monster:
    def fighting(self):
        action = choice(["Монстр закрылся щитом.", "Монстр ранен. Он не может бить.", "Монстр убит."])
        print(action)

class Battle:
    def __init__(self, monster, fighter):
        self.monster = monster
        self.fighter = fighter

    def fighter_vs_monster(self):
        self.fighter.weapon.attack(self.fighter)
        self.monster.fighting()

sword = Sword("меч")
bow = Bow("лук")
axe = Axe("топор")
halberd = Halberd("алебарда")

m1 = Monster()
f1 = Fighter("Ярополк", bow)
f1.changeWeapon(axe)
battle1 = Battle(m1, f1)
battle1.fighter_vs_monster()
print("")
m2 = Monster()
f2 = Fighter("Добрыня", bow)
f2.changeWeapon(sword)
battle2 = Battle(m2, f2)
battle2.fighter_vs_monster()
print("")
m3 = Monster()
f3 = Fighter("Вольбран", bow)
f3.changeWeapon(halberd)
battle3 = Battle(m3, f3)
battle3.fighter_vs_monster()
