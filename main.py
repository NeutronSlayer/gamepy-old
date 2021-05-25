from classes.classes import Person, BColors, Spell

running = True
run = True
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

def spell_damage():
    print(BColors.Green +
          spell.name + 'spell deals for ' + str(magic_damage) +
          ' points of damage.' +
          BColors.ResetAll)
    player_mp = player.reduce_mp(spell.cost)
    player_current_mp = player_mp

    enemy_HP = enemy.take_damage(magic_damage)
    run = False


while running:
    global enemy_HP
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

        player_mp = player.get_mp()
        spell = player.magic[magic_choice_index]
        magic_damage = spell.generate_spell_damage()

        run = True

        while run:

            if spell.cost < player_mp:
                print(BColors.Green +
                      spell.name + 'spell deals for ' + str(magic_damage) +
                      ' points of damage.' +
                      BColors.ResetAll)
                player_mp = player.reduce_mp(spell.cost)
                player_current_mp = player_mp

                enemy_HP = enemy.take_damage(magic_damage)
                run = False

            elif player_mp == spell.cost:
                print(BColors.Green +
                      spell.name + 'spell deals for ' + str(magic_damage) +
                      ' points of damage.' +
                      BColors.ResetAll)
                player_mp = player.reduce_mp(spell.cost)
                player_current_mp = player_mp
                enemy_HP = enemy.take_damage(magic_damage)
                run = False

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
    print("Players current MP:", player_current_mp, '/', player.get_max_mp())
    print('-----------------------------------------')

    if enemy.get_hp() == 0:
        print(BColors.Green + '!!!You WON!!!' +
              BColors.ResetAll)
        running = False

    elif player.get_hp() == 0:
        print(BColors.Red + 'Your\' enemy defeated you' +
              BColors.ResetAll)
        running = False
