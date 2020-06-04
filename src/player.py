# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,location,characterClass,items):
        self.name = name
        self.location = location
        self.items = items
        self.characterClass = characterClass
    
    def __str__(self):
        return f"Player {self.name}, currently in room: { self.location }, currently has:{self.items}"
    
    def listItems(self):
        joinedItems = self.items.join("\n")
        return f"Your items: {joinedItems}"
    