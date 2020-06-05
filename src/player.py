# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,location,characterClass):
        self.name = name
        self.location = location
        self.items = []
        self.characterClass = characterClass
    
    def __str__(self):
        return f"Player {self.name}, currently in room: { self.location }, currently has:{self.items}"
    
    def listItems(self):
        allTheItemsThisPlayerHas = ""
        for items in self.items:
            allTheItemsThisPlayerHas += items.__str__()
        return allTheItemsThisPlayerHas
    
    def takeItem(self,item):
        self.items.append(item)
    