# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, items, current_room=None):
        self.current_room = current_room
        self.items = items

    def inventory(self):
        if len(self.items) > 0:
            player_items = [item.name for item in self.items]
            return player_items
        else:
            print("Nothing in inventory")

    def pick_up_item(self, item):
        self.items.append(item.name)
        print(self.items)

    def drop_item(self, item):
        self.items = list(
            filter(lambda x: x.name is not item.name, self.items))