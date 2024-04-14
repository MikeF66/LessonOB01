class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f'{other.name} потерял {self.attack_power} очков здоровья и у него осталось всего {other.health} очков')

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:  # если turn - четное значение - очередь игрока (player)
                print(f'Нападает игрок {self.player.name}')
                self.player.attack(self.computer)
            else:              # если turn - нечетное значение - очередь компьютера
                print(f'Нападает компьютер {self.computer.name}')
                self.computer.attack(self.player)
                print(f'Ход компьютера {self.computer.name}')
                self.computer.attack(self.player)
            if not self.computer.is_alive():
                print(f'{self.player.name} победил!')
                break
            if not self.player.is_alive():
                print(f'{self.computer.name} победил!')
                break
            turn += 1

    player = Hero("Mike")
    computer = Hero("Comp")
    game = Game(player, computer)
    game.start()








