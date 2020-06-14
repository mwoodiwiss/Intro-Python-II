from room import Room
from player import Player
from items import Item

# Declare all the rooms

outside =  Room("Outside Cave Entrance",
"North of you, the cave mount beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

items = {
    "dagger": Item("dagger", "small bladed knife")
}

outside.items.append(items["dagger"])

# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

def Move(player, user_input):
    if hasattr(player.current_room, f'{user_input}_to'):
        player.current_room = getattr(player.current_room, f'{user_input}_to')
    if hasattr(player.current_room, f'{user_input}_to') == 'false':
        print("Can't move in that direction.")

def Quit(player, user_input):
    confirm_quit = input('\nAre you sure you want to quit?\nyes/no\n')
    if confirm_quit == 'yes': 
        quit()
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player([])
player.current_room = outside
# player.items.append(dagger)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    print("\n")
    print(player.current_room)
    print(f"Current room has {player.current_room.inventory()}")
    user_input = input("\nEnter (n), (s), (e), (w) to MOVE, grab, to GRAB, drop, to DROP, or (q) to quit: ").lower()

    choice_arr = user_input.split(" ")
    choice_len = len(choice_arr)

    if user_input in {'n', 's','e', 'w'}:
        Move(player, user_input)
    if choice_len == 2:
        action = choice_arr[0]
        item = choice_arr[1]
        if action in ["grab"]:
            try:
                player.pick_up_item(items[item.name])
                print(items[item] + 'line 82')
            except:
                print("No item to grab")
        if action in ["drop"]:
            try:
                player.drop_item(item)
            except:
                print("No item to drop")     
    if user_input == 'q':
        Quit(player, user_input)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
