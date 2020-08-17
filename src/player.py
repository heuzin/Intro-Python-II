# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, current_room):
        # Store current_room as a Room object
        self.current_room: Room = current_room
        self.items = []

    def show_inventory(self):
        print(f'\nItems in inventory:')
        for item in self.items:
            print(item)

    def get_item(self, item_name: str):
        for item in self.items:
            if item_name.lower() == item_name.lower():
                return item

            return None
    
    def remove_item(self, item):
        self.items.remove(item)