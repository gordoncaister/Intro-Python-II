from room import Room
from textwrap import wrap 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = {
    "name": "gordon",
    "room": "outside",
    "class": "strider"
}

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
print(room[player["room"]].describeRoom())

direction = str(input("Enter a cardinal direction: N, E, S, W to travel in that direction or Q to quit\n")).lower()


while not direction == 'q':
    if direction == "n":
        try:
            for currentRoom in room:
                if room[currentRoom] == room[player["room"]].n_to:
                    player["room"] = currentRoom
                    break
            print("You go North\n")
            print(room[player["room"]].describeRoom())
        except AttributeError:
            print("There is nothing to the North")
    elif direction == "e":
        try:
            for currentRoom in room:
                if room[currentRoom] == room[player["room"]].e_to:
                    player["room"] = currentRoom
                    break
            print("You go East\n")
            print(room[player["room"]].describeRoom())
        except AttributeError:
            print("There is nothing to the East")
    elif direction == "s":
        try:
            for currentRoom in room:
                if room[currentRoom] == room[player["room"]].s_to:
                    player["room"] = currentRoom
                    break
            print("You go South\n")
            print(room[player["room"]].describeRoom())
        except AttributeError:
            print("There is nothing to the South")
    elif direction == "w":
        try:
            for currentRoom in room:
                if room[currentRoom] == room[player["room"]].w_to:
                    player["room"] = currentRoom
                    break
            print("You go West\n")
            print(room[player["room"]].describeRoom())
        except AttributeError:
            print("There is nothing to the West")
    else:
        print("Please enter a valid direction")

    direction = str(input("Enter a cardinal direction: N, E, S, W to travel in that direction or q to quit\n")).lower()
    print("\n\n")