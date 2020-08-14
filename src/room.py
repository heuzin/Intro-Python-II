# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # 1) Adding these as attributes in the constructor is optional; 
        # in python you can arbitrarily set attributes on instances
        # 2) the `: Room` syntax is a typehint. It just serves as a reminder
        # for other developers that self.n_to is storing a Room object (as opposed to a str)
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

    def print_items(self):
        for item in self.items:
            print(f"You find a {item.name.lower()} in this room!")

    def find_item(self, input_item):
        for item in self.items:
            if item.name.lower() == input_item.lower():
                return item
            return None

    def remove_item(self, item):
        print(f"You have picked up the {item.name.lower()}")
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)
        print(f"You have dropped the {item.name.lower()}")

class Dark_Room(Room):
    def __init__(self, name, description, items, visibility):
        super().__init__(name, description, items)
        self.visibility = visibility

    def light_on(self):
        self.visibility = True