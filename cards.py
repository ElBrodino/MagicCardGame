from magicColor import *

class Card:
    def __init__(self):
        self.type = ""
        self.artist = ""
        self.tapped = False
        self.color = Magic_color()
        self.isPermanent = False
        self.cost = None

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = True

class Land(Card):
    def __init__(self, color):
        super().__init__()
        self.type = "land"
        self.color = color

class Creature(Card):
    def __init__(self, name, race, cost, color, power, strength):
        super(Creature, self).__init__()
        self.race = race
        self.name = name
        self.type = "creature"
        self.color = color
        self.cost = cost
        self.power = power
        self.strength = strength
        self.life = strength
        self.dead = False

    def attack(self, target):
        target.life -= self.power
        if target.strength <= 0:
            target.die()

    def die(self):
        self.dead = True

class Enchantment(Card):
    def __init__(self, cost, color):
        super().__init__()
        self.cost = cost
        self.color = color


if __name__ == '__main__':
    card1 = Land(Green)
    print(card1.type)
    print(type(card1))
    print(type(card1) == Land)

    creature1 = Creature(name="Blue Lagoon Triton", race="fish", cost=1, color=Blue, power=2, strength=2)
    creature2 = Creature(name="Red-face trouduc", race="Goblin", cost=1, color=Red, power=1, strength=1)

    creature1.attack(creature2)
    print("Is", creature2.name, "dead ?", creature2.dead)
    print(creature2.name, "life:", creature2.life)
