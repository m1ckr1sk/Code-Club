#!/bin/python3
import time
import json


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


def get_monster_countdown():
    time_now = time.time()
    time_to_go = monster_clock - time_now
    return time_to_go


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
    if "monster" in rooms[currentRoom]:
        if not monster_clock_set:
            print('A {}! You have 5 seconds to escape'.format(rooms[currentRoom]['monster']['name']))
        else:
            print('A {}! You have {:5.2f} seconds to escape'.format(rooms[currentRoom]['monster']['name'],
                                                                    get_monster_countdown()))
    print("---------------------------")


def print_current_room():
    top = "-----------"
    mid1 = "|         |"
    mid2 = "|    X    |"
    mid3 = "|         |"
    bottom = "-----------"


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other room positions
rooms = data = json.load(open('rooms.json'))

# start the player in the Hall
currentRoom = 'Hall'
monster_clock_set = False

show_instructions()

# loop forever
while True:
    print("{} uh".format(monster_clock_set))
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

    if monster_clock_set:
        # check the clock
        if get_monster_countdown() < 0:
            print('The monster has got you... GAME OVER!')
            break

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

    wielding_weapon = None
    if move[0] == 'use':
        weapon_to_use = ' '.join(move[1:])
        if weapon_to_use in inventory:
            wielding_weapon = weapon_to_use
            print("You use the {}....".format(weapon_to_use))

    # player loses if they enter a room with a monster and do not move in 5 seconds
    if 'monster' in rooms[currentRoom]:
        if not monster_clock_set:
            monster_clock_set = True
            monster_clock = time.time()  + 5
        else:
            if wielding_weapon:
                if rooms[currentRoom]['monster']['iskilledby'] == wielding_weapon:
                    monster_killed = rooms[currentRoom]['monster']['name']
                    print("and the {} is slaughtered!".format(monster_killed))
                    del rooms[currentRoom]['monster']
                    monster_clock_set = False
                else:
                    print("..but the {} repels it".format(rooms[currentRoom]['monster']['name']))
    else:
        monster_clock_set = False

    # player wins if they get to the garden with a key and a shield
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
