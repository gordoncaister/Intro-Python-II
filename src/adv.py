from room import Room
from textwrap import wrap 
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons","outside"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""","foyer"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",'treasure'),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = {
#     "name": "gordon",
#     "room": "outside",
#     "class": "strider"
# }
player = Player("gordon","outside","strider")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#welcome
print("Welcome to Hoard")
print("A text based hoarding adventure game.\n")
print(room[player.location].describeRoom())

direction = ""
noun = None
# str(input("Enter a cardinal direction: N, E, S, W to travel in that direction or Q to quit\n")).lower()
itemsInRoom = room[player.location].listItems()

while not direction == 'q':
    if direction == "n":
        if not room[player.location].n_to(player.location) == None:
            player.location = room[player.location].n_to(player.location)
            print("You go North\n")
            print(room[player.location].describeRoom())
        else:
            print("There is nothing to the North")
        
    elif direction == "e":
        if not room[player.location].e_to(player.location) == None:
            player.location = room[player.location].e_to(player.location)
            print("You go East\n")
            print(room[player.location].describeRoom())
        else:
            print("There is nothing to the East")

    elif direction == "s":
        if not room[player.location].s_to(player.location) == None:
            player.location = room[player.location].s_to(player.location)
            print("You go South\n")
            print(room[player.location].describeRoom())
        else:
            print("There is nothing to the South")

    elif direction == "w":
        if not room[player.location].w_to(player.location) == None:
            player.location = room[player.location].w_to(player.location)
            print("You go West\n")
            print(room[player.location].describeRoom())
        else:
            print("There is nothing to the West")

    elif direction == "look":
        itemsInRoom = room[player.location].listItems()
        if not itemsInRoom == "":
            print(f"Here are all the items in the room: {itemsInRoom}")
        else:
            print("You look around, but it's just kind of bare. There are no items here.\n")
    elif direction == "":
        pass
    elif direction == "take" and not noun == None:
        # if room[player.location].itemsInRoom
        itemsInRoom = room[player.location].itemsinroom
        itemInRoom = False
        for items in itemsInRoom:
            if noun in items.name:
                print(f"You take the {noun}")
                room[player.location].itemsinroom.remove(items)
                player.items.append(items)
                itemInRoom = True
        if itemInRoom == False:
            print(f"You're looking for an item called: {noun}, but it doesn't exist in this room.\n")
        
    else:
        print("Please enter a valid direction")

    direction = str(input("Enter a cardinal direction: N, E, S, W to travel in that direction or q to quit\nYou can also use look to look around, if you find an item:\nTry typing 'take itemname' replacing itemname with the name of the item\n")).lower()

    splitCommand = direction.split(" ")

    direction = splitCommand[0]
    if len(splitCommand) > 1:
        noun = splitCommand[1]
    else:
        noun = None
    
    print("\n")


