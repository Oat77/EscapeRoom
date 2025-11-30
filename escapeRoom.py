import random
#Destinations to be assigned to doors
destinations = ["Bedroom", "Bathroom", "Living Room", "Kitchen", "Basement", "Outside"]

#Special items
random_items = ["painting", "doormat", "doll", "medicine", "vaccum", "block", "laptop", "fan", "teacup", "headphones", "gun", "knife", "glasses"]

#List responsible for storing 'Door' objects
room_doors = []

#Standard items that will be assigned to each room.
room_items = {

    "Bedroom": ["hanger", "humidifier", "book", "lamp"],
    "Bathroom": ["soap", "rag", "towel", "toothbrush"],
    "Living Room": ["cushion", "remote", "pen", "shoe"],
    "Kitchen": ["fork", "dish", "spoon", "bin"],
    "Basement": ["broom", "safe", "chest", "toolkit"]

}

#Player class
class Player:

    def __init__(self, name):
        self.name = name


#Door class
class Door:  

    def __init__(self, dest):
        self.dest = dest

    def door_dest(self):
        return f"This door leads to the {self.dest}."


#Creats a list of two 'Door' objects tied to each destination in the 'destinations' list.
#Ensures that only one outside Door object is created. 
for dest in destinations:
    if dest == "Outside":
        room_doors.append(Door(dest))
        continue
    else:
        room_doors.append(Door(dest))
        room_doors.append(Door(dest))


#Creates a parent Room class that initializes with a list of items, two doors and a random special item. 
class Room: 

    def __init__(self, items, door_1= random.choice(room_doors), door_2= random.choice(room_doors), special_item= random.choice(random_items)):
        self.door1 = door_1
        self.door2= door_2
        self.special_item = special_item
        self.items= items

    def roomitems(self):
        return f"This room has the following items: {self.items}."
    
    def specialitem(self):
        return f"This room has this special item: {self.special_item}."



#Creates sub classes of the Room parent class. 
#Assigns an item list based on room type. 
class Bedroom(Room): 
    def __init__(self): 
        super().__init__(items= room_items["Bedroom"])
        
        
class Bathroom(Room): 
    def __init__(self): 
        super().__init__(items= room_items["Bathroom"])
  
class LivingRoom(Room): 
    def __init__(self): 
        super().__init__(items= room_items["Living Room"])


class Kitchen(Room): 
    def __init__(self): 
        super().__init__(items= room_items["Kitchen"])

class Basement(Room): 
    def __init__(self): 
        super().__init__(items= room_items["Basement"])

""" test= Bedroom()
assigned= test.door1.door_dest()
assigned2= test.door2.door_dest()
print (assigned)
print (assigned2)
print ("_____________________________")


room_doors.remove(test.door1)
room_doors.remove(test.door2)
for i in room_doors:
    print (i.door_dest())
 """


