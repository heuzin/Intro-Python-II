from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

itemKnife = Item('Knife', 'Sharp thing')
room['outside'].items.append(itemKnife)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input('Choose a name for your character:\n')
player = Player(room['outside'])

# Write a loop that:
#
while True:
    # * Prints the current room name
    current_room = player.current_room
    print(f'\n{player_name} -', player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    #room items
    if current_room.items:
        for item in current_room.items:
            print(item)
    # * Waits for user input and decides what to do.
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w'), 'get' to pick up an item and 'drop' to drop an item: \n")
    split_input = user_input.split()
    # If the user enters a cardinal direction, attempt to move to the room there.
    attribute = user_input + "_to"
    if len(user_input) < 1:
        print('\nControls: \nN,S,E,W to move to a different room.')
    elif user_input in 'nsew':
        if getattr(current_room, attribute): 
        # if current_room.n_to is not None:
            player.current_room = getattr(current_room, attribute)
        else: 
            print(f'\nNo place to {user_input}, please choose a valid direction')
            continue
    elif len(split_input) == 2:
        item_name = split_input[1]
        if split_input[0].lower() == 'get':
            # If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.
            item = current_room.get_item(item_name)
            if item:
                item.on_take()
                # remove the item from the room
                current_room.remove_item(item)
                # Add it to the player's items
                player.items.append(item)
            else:
                print(f"\n{item_name} does not exist in room")
        elif split_input[0] == 'drop':
            # drop the item
            item = player.get_item(item_name)
            # check if item is on player
            # if it is:
            if item:
            #   call item.on_drop()
                item.on_drop()
            #   remove from player
                player.remove_item(item)
            #   add to room
                current_room.items.append(item)
            else:
                print(f"\nYou don't have that item in your inventory.")
    # If the user enters "q", quit the game.
    elif user_input == 'q':
        break
    # Print an error message if the movement isn't allowed.
    else:
        print('\nControls: \nN,S,E,W to move to a different room.')
        continue