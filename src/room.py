from item import Item


northDictionary = {
    "outside":"foyer",
    "foyer":"overlook",
    "narrow":"treasure"
}

eastDictionary = {
    "foyer":"narrow",
}

westDictionary = {
    "narrow":"foyer",
}

southDictionary = {
    "foyer":"outside",
    "treasure":"narrow",
    "overlook":"foyer"
}

itemsList = {
    "foyer":[
            Item("spoon","Nestled in the crannies of the foyer you find a rusty spoon, maybe it was once used to ladel soup into the gullet of a long lost king?"),
            Item("button", "Not a big red button, no this is a button, from like a shirt. It's probably worthless to you. But as they say, one mans trash is another man's treasure.")
        ],
    "overlook":[
        Item("sword","There just below the outcropping is a sword, the perfect weapon for a corridor encounter")
        ],
    "narrow":[
        Item("candle","I don't know how you missed it before, but there is an already lit candle just sitting here in the narrow passage.")
        ]
}


# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description,roomName):
        self.name = name
        self.description = description
        self.itemsinroom =  []
        if roomName in itemsList:
            self.itemsinroom = itemsList[roomName]
        # if self.itemsinroom.len() != 0:
        

    def __str__(self):
        return f"{self.name}, {self.description}"

    def describeRoom(self):
        return f"Your current location: \n{self.name}.\n{self.description}\n\n"

    def n_to(self, currRoom):
        if currRoom in northDictionary:
            return northDictionary[currRoom]
        else:
            return None

    def e_to(self, currRoom):
        if currRoom in eastDictionary:
            return eastDictionary[currRoom]
        else:
            return None

    def w_to(self,currRoom):
        if currRoom in westDictionary:
            return westDictionary[currRoom]
        else:
            return None

    def s_to(self,currRoom):
        if currRoom in southDictionary:
            return southDictionary[currRoom]
        else:
            return None

    def listItems(self):
        itemsNameAndDescription = ""
        for items in self.itemsinroom:
            itemsNameAndDescription+= items.__str__()
        return itemsNameAndDescription
    