import random
from classes.magic import Spell


class BColors:
    ResetAll = "\033[0m"

    Bold = "\033[1m"
    Dim = "\033[2m"
    Underlined = "\033[4m"
    Blink = "\033[5m"
    Reverse = "\033[7m"
    Hidden = "\033[8m"

    ResetBold = "\033[21m"
    ResetDim = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink = "\033[25m"
    ResetReverse = "\033[27m"
    ResetHidden = "\033[28m"

    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"

    BackgroundDefault = "\033[49m"
    BackgroundBlack = "\033[40m"
    BackgroundRed = "\033[41m"
    BackgroundGreen = "\033[42m"
    BackgroundYellow = "\033[43m"
    BackgroundBlue = "\033[44m"
    BackgroundMagenta = "\033[45m"
    BackgroundCyan = "\033[46m"
    BackgroundLightGray = "\033[47m"
    BackgroundDarkGray = "\033[100m"
    BackgroundLightRed = "\033[101m"
    BackgroundLightGreen = "\033[102m"
    BackgroundLightYellow = "\033[103m"
    BackgroundLightBlue = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan = "\033[106m"
    BackgroundWhite = "\033[107m"


class Person:
    def __init__(self, hp, mp, attack, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = attack - 10
        self.atkh = attack + 10
        self.df = df
        self.magic = magic
        self.action = ['Attack', 'Magic']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def reduce_mp(self, cost):
        self.mp -= cost

    def show_action(self):
        i = 1
        for item in self.action:
            print(str(i) + ':', item)
            i += 1

    def show_magic(self):
        i = 1
        for spell in self.magic:
            print(str(i) + ':', spell.name, spell.cost)
            i += 1

    def healing_spell_use(self):
        self.hp = self.maxHp
        return self.hp

    def heal(self, damage):
        self.hp += damage
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        return self.hp

    def enemy_random_action(self):
        enemy_random_numbers = random.randrange(0, 2)
        return enemy_random_numbers







'''
from classes.classes import Person, BColors, Spell

running = True
i = 0

# Instantiating Black magic spells
fire = Spell('Fire', 10, 100, 'Black')
thunder = Spell('Thunder', 10, 100, 'Black')
blizzard = Spell('Blizzard', 10, 100, 'Black')
meteor = Spell('Meteor', 20, 200, 'Black')
quake = Spell('Quake', 14, 140, 'Black')
# Instantiating White magic spells
cure = Spell('Cure', 12, 120, 'White')
cura = Spell('Cura', 18, 200, 'White')

# Instantiating game characters
player = Person(1000, 665, 60, 34, [fire, thunder, blizzard, meteor, quake])
enemy = Person(1000, 65, 60, 34, [fire, thunder, blizzard, meteor, quake])


print(BColors.Bold + BColors.Red + 'An Enemy Attacks' + BColors.ResetAll)

while running:
    global enemy_HP, player_current_mp
    print('===================================================================')
    print(BColors.Blue + BColors.Underlined + 'ACTIONS:' + BColors.ResetAll)
    player.show_action()
    player_action_index = int(input('MAKE YOUR DECISION:')) - 1

    if player_action_index == 0:
        player_damage = player.generate_damage()
        enemy_HP = enemy.take_damage(player_damage)

        print(BColors.Green + "You've attacked for:" + str(player_damage) +
              BColors.ResetAll)

    elif player_action_index == 1:
        player.show_magic()
        magic_choice_index = int(input('Please choose your magic:')) - 1

        spell = player.magic[magic_choice_index]
        magic_damage = spell.generate_spell_damage()
        player_current_mp = player.get_mp()
        run = True

        while run:
            if player_current_mp > spell.cost:
                print(BColors.Green +
                      spell.name + 'spell deals for ' + str(magic_damage) +
                      ' points of damage.' +
                      BColors.ResetAll)
                player_current_mp = player.reduce_mp(spell.cost)
                enemy_HP = enemy.take_damage(magic_damage)

            elif player_current_mp == spell.cost:
                print(BColors.Green +
                      spell.name + 'spell deals for ' + str(magic_damage) +
                      ' points of damage.' +
                      BColors.ResetAll)
                player_current_mp = player.reduce_mp(spell.cost)
                enemy_HP = enemy.take_damage(magic_damage)

            else:
                print(BColors.Yellow +
                      'You don\'t have enough magic points.' +
                      BColors.ResetAll)
                continue

    else:
        print(BColors.Yellow +
              'INVALID' +
              BColors.ResetAll)
        continue

    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    enemy_current_mp = enemy.get_mp()
    player_HP = player.take_damage(enemy_damage)
    print(BColors.LightRed +
          "Enemy attacked for:" + str(enemy_damage) +
          BColors.ResetAll)

    print('-----------------------------------------')
    print("Enemy's HP:" + str(enemy_HP) + '/' + str(enemy.get_max_hp()))
    print("Enemy's MP:" + str(enemy_current_mp) + '/' + str(enemy.get_max_mp()) + '\n')
    print('Player\'s HP:', str(player_HP), '/', str(player.get_max_hp()))
    print("Players current MP:", str(player_current_mp), '/', player.get_max_mp())
    print('-----------------------------------------')

    if enemy.get_hp() == 0:
        print(BColors.Green + '!!!You WON!!!' +
              BColors.ResetAll)
        running = False

    elif player.get_hp() == 0:
        print(BColors.Red + 'Your\' enemy defeated you' +
              BColors.ResetAll)
        running = False

'''