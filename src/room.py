# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__ (self, name, description):
        self.name = name 
        self.description = description
        self.items = []
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.n_to = None

    def inventory(self):
        if len(self.items) > 0:
            rooms_items = [item.name for item in self.items]
            return rooms_items
        else:
            print("Nothing in inventory")

    def __str__(self):
        output = f'{self.name}: {self.description}\n'
        if self.s_to:
            output += 'To the south is: ' + self.s_to.name + '\n'
        if self.e_to:
            output += 'To the east is: ' + self.e_to.name + '\n'
        if self.n_to:
            output += 'To the north is: ' + self.n_to.name + '\n'
        if self.w_to:
            output += 'To the west is: ' + self.w_to.name + '\n'

        return output