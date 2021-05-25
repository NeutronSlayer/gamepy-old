import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self. cost = cost
        self.dmg = dmg
        self.type = type

    def generate_spell_damage(self):
        mgl = self.dmg - 5
        mgh = self.dmg + 5
        random_damage = int(random.randrange(mgl, mgh))
        return random_damage

    def get_spell_name(self):
        return self.name

    def get_spell_mp_cost(self):
        return self.cost
