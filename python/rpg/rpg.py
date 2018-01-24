#!/bin/python3


def show_instructions():
    # print a main menu and the commands
    print('''
RPG Game
========

Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
  go [direction]
  get [item]
''')


def show_status():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print("Inventory : " + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        for item in rooms[currentRoom]['item']:
            print('You see a ' + item)
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other room positions
rooms = {

    'Hall': {'south': 'Kitchen',
             'east': 'Dining Room',
             'item': ['key']
             },

    'Kitchen': {'north': 'Hall',
                'item': ['monster']
                },

    'Dining Room': {'west': 'Hall',
                    'south': 'Garden',
                    'item': ['potion','brussel sprout']
                    },

    'Garden': {'north': 'Dining Room'}

}

# start the player in the Hall
currentRoom = 'Hall'

show_instructions()

# loop forever
while True:

    show_status()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()
    command = move[0]


    # if they type 'go' first
    if command == 'go':
        direction = ' '.join(move[1:])
        # check that they are allowed wherever they want to go
        if direction in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][direction]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        item_to_get = ' '.join(move[1:])
        # if the room contains an item, and the item is the one they want to get
        if 'item' in rooms[currentRoom] and item_to_get in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [item_to_get]
            # display a helpful message
            print(item_to_get + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + item_to_get + '!')

    # player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # player wins if they get to the garden with a key and a shield
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
