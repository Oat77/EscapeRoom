import random
random.seed()

questions= {
    "How many parishes are there in Jamaica": 14,
    "How many continents are there on the planet?": 7,
    "How many planets are in the solar system?": 8,
    "How many bones are there in the humna body?": 206,
    "How many states are in the United States?": 50,
    "True or False: The elephant is the largest mammal on earth.": "false",
    "What was the year of jamaica's independence?": 1962,
    "What is the capital of Japan?": "tokyo",
    "What is the highest mountain in the world?": "mount everest",
    "What does CPU stand for?": "central processing unit",
    "Which country has won the most World Cups?": "brazil",
    "What is the only mammal capable of true flight?": "bat",
    "Who was the first Disney princess?": "snow white",
    "Which Disney movie has had the most sequels?": "toy story"
}


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

    def __init__(self, items):
        self.special_item = random.choice(random_items)
        self.items= items
        self.location= [key for key, value in room_items.items() if value== self.items][0]
        if self.location == "Bathroom":
            room_doors[:]= [d for d in room_doors if d.dest != "Outside"]
        self.door1= random.choice(room_doors)
        room_doors.remove(self.door1)
        self.occupied= False
        
        #Sublist containing doors whose destinations are not the same as door1
        remaining_doors= [door for door in room_doors if door.dest != self.door1.dest]

        #Assigns door2 and removes it from the global list of doors. 
        self.door2= random.choice(remaining_doors)
        room_doors.remove(self.door2)
        
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

#Player class
class Player:
    def __init__ (self, name, starting_room):
        self.name=name
        self.inventory= []
        self.currentLocation= starting_room
        
    def confirm_location(self):
        print (f"The player is now in the {self.currentLocation.location}.")

    #Moves player from one room to another.
    def player_move(self, door):
        for room in roomList:
            if room.location == door.dest:
                self.currentLocation = room
                break

    #Picks up item. 
    def item_pickup(self, item):
        self.inventory.append(item)
        print(f"You have successfully retrieved the {item}! ")

    #Displays player inventory
    def show_inventory(self):
        print (f"Player's inventory: {self.inventory}.")



while True: 
    print("##########################")
    print("# Welcome to the escape room! #")
    print("##########################")

    print("Game Rules:\n")

    print("1: You must find a way to exit the house.")
    print("2. The house has 5 areas Bedroom, Bathroom, Living Room, Kitchen, Basement")
    print("3. Each Area Has two doors Each leading to another Area")
    print("4. One Room Will have a door leading outside. The door is assigned randomly at the beginning of the game.")
    print("5. The Bathroom Cannot Lead outside. ")
    print("6. You have 7 doors to open before you get caught")
    print("7. Once your lives get to zero the game ends or if you escape\n \n ")

    startgame= input("Would you like to begin the game? (Enter 1 for 'Yes' or 2 for 'No')")

    if startgame == "1":
        playerLives= 7
        bedroom= Bedroom()
        bathroom= Bathroom()
        livingroom=  LivingRoom()
        kitchen= Kitchen()
        basement= Basement()

        roomList= [bedroom, bathroom, livingroom, kitchen, basement]

        playerName= input("Enter player name: ")
        player1= Player(playerName, random.choice(roomList))

        while playerLives > 0:
            player1.confirm_location()
            print (player1.currentLocation.roomitems())
            search_request= input ("There may be a special item here, do you want to search? (Y or N): ")
            if search_request.lower == "y":
                print (player1.currentLocation.specialitem())
                room_special= player1.currentLocation.special_item
                collect_request= input("Woudd you like to collect this item? (Y or N): ")
                if collect_request.lower() =='y':
                    randomQuestion= random.choice(list(questions.keys()))
                    answer = questions[randomQuestion]
                    quiz= int(input(randomQuestion))
                    try:
                        if type(quiz)== int:
                            continue
                        elif type(quiz) == str:
                            quiz = quiz.lower().strip()
                    except TypeError:
                        print("Incorrect answer format.")
                    if quiz == answer:
                        player1.item_pickup(room_special)
                    else:
                        print ("Oops. Wrong answer... you lost a life. ")
                        playerLives-= 1
                else: 
                    continue
            
            print (f"Door 1: {player1.currentLocation.door1.door_dest()}.\n")
            print (f"Door 2: {player1.currentLocation.door2.door_dest()}. \n")
            playerMove= input ("Choose your door (1 or 2): \n")
            if playerMove == "1":
                print ("Moving to the next room...\n \n")
                if player1.currentLocation.door1.dest== "Outside":
                    print ("You escaped!")
                    break
                else:
                    player1.player_move(player1.currentLocation.door1)
                    player1.confirm_location()
            elif playerMove == "2": 
                print ("Moving to the next room...\n \n")
                if player1.currentLocation.door2.dest== "Outside":
                    print ("You escaped!")
                    break
                else:
                    player1.player_move(player1.currentLocation.door2)
                    player1.confirm_location()
            playerLives-=1 
    else:
        break
            
            




# player1= Player("Omaro", random.choice(roomList))
# print (player1.currentLocation)


""" 
bedroom_assigned= bedroom.door1.door_dest()
bedroom_assigned2= bedroom.door2.door_dest()

print ("-------")
bathroom_assigned= bathroom.door1.door_dest()
bathroom_assigned2= bathroom.door2.door_dest()

print ("---------------")


print (bedroom_assigned)
print (bedroom_assigned2)
print ("_____________________________")

print (bathroom_assigned)
print (bathroom_assigned2)

print ("------------------")


for i in room_doors:
    print (i.door_dest()) """



