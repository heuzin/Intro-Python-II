class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name}: {self.description}'

    def on_take(self):
        print(f'You have picked up {self.name}')

# class LightTorch(Item):
#     def __init__(self, name, description, isOn=False):
#         super().__init__(name, description)
#         self.isOn = isOn
    
#     def __str__(self):
#         return f'{self.name}'