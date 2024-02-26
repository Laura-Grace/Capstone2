from Capstone2.character import Enemy

dave = Enemy('Dave', 'A smelly zombie')

dave.describe()

dave.set_conversation('The walking dead is problematic and zom-phobic.')

dave.talk()

dave.set_weakness('cheese')

print('What will you fight with?')
fight_with = input()
dave.fight(fight_with)