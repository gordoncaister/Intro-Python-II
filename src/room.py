
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

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
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
    