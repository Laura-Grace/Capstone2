from Capstone2.room import Room
from Capstone2.character import Enemy
from Capstone2.character import Friend


print("Welcome to the bootcamp Text Based Adventure Game!")
print()
kitchen = Room('kitchen')
ballroom = Room('ballroom')
dining_hall = Room('dining hall')

kitchen.set_description("A dark and dirty room buzzing with flies. There is a locked door, does it lead outside?")

ballroom.set_description('A cavernous room filled with doll heads.')

dining_hall.set_description('Contains a long table lit by a single candle.')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('The Walking dead is Zom-Phobic')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

eva = Friend('Eva', 'A Doll with a severed neck')
eva.set_conversation('Have you seen my eye?')
ballroom.set_character(eva)

current_room = kitchen

key_aquired = False

def get_key():
    return key_aquired

while True: 
    print('\n')
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input('> ')

    if command == 'exit':
        break

    if command in ['north', 'south', 'east', 'west']:
        current_room = current_room.move(command)
    elif command == 'talk':
        if isinstance(dave, Enemy) == True and current_room == dining_hall:
            dave.talk()
        elif isinstance(eva, Friend) == True and current_room == ballroom:
            eva.talk()
    elif command == 'fight':
        if isinstance(dave, Enemy) == True and current_room == dining_hall:
            if not dave.fight('cheese'):
                print('You have been defeated. Game over!')
                break
        else: 
            print('You can not fight this character')
    elif command == 'hug':
        if isinstance(eva, Friend) == True and current_room == ballroom:
            eva.hug()
        else:
            print('I will kil you.')
    elif command == 'key':
        if isinstance(dave, Enemy) == True and current_room == dining_hall:
            print('You will never escape me.')
        if isinstance(eva, Friend) == True and current_room == ballroom:
            print('Only because you asked nicely!')
            key_aquired = True
    elif command == 'open':
        if current_room == kitchen:
            if get_key() == False:
                print('You need a key to open this door.')
            elif get_key() == True:
                print('You escape the haunted mansion!')
                break
            else: 
                print('What door?')
        else: 
            print('What door?')


