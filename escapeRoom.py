""" Full Name: Omaro Taylor
ID Number: 20251415
Course Name: Python Programming (ITT212)
Lecturer Name: Stefan Watson
Semester: Fall 2025 """

import random
random.seed()

#Question repository for special items.
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


#Creates a parent Room class that initializes with a list of items, two doors and a random special item. 
class Room: 

    def __init__(self, items):
        self.special_item = random.choice(random_items)
        self.items= items

        #Assigns location of the room baased on the location of the assigned set of items. 
        self.location= [key for key, value in room_items.items() if value== self.items][0]

        #Creates creates a door for each room.
        #Ensures that the Bathroom does not get an outside door.
        if self.location == "Bathroom":
            available_doors= [d for d in room_doors if d.dest != "Outside"]
        else:
            available_doors = room_doors[:]

        #Assigns a random door to the room
        #Removes said door from door list to prevent reassignment.
        self.door1= random.choice(available_doors)
        room_doors.remove(self.door1)
        self.occupied= False
        
        #Sublist containing doors whose destinations are not the same as door1
        remaining_doors= [door for door in available_doors if door.dest != self.door1.dest]

        #Assigns door2 and removes it from the global list of doors. 
        self.door2= random.choice(remaining_doors)
        room_doors.remove(self.door2)
        
    #Displays room items and special items respectively. 
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
        print (f"{self.name} is now in the {self.currentLocation.location}.")

    #Moves player from one room to another.
    def player_move(self, door):
        for room in roomList:
            if room.location == door.dest:
                self.currentLocation = room
                break

    #Picks up item. 
    def item_pickup(self, item):
        if len(self.inventory)<3:
            self.inventory.append(item)
            print(f"You have successfully retrieved the {item}! ")
        else: 
            print("Your inventory is full. You cannot carry any more items.")

    #Displays player inventory
    def show_inventory(self):
        print (f"Player's inventory: {self.inventory}.")



#Initialization of game UI
game_over= False

#Welcome menu
while not game_over: 
    print("##########################")
    print(" WELCOME TO THE ESCAPE ROOM!")
    print("########################## \n")

    print("Game Rules:\n")

    print("1: You must find a way to exit the house.")
    print("2. The house has 5 areas Bedroom, Bathroom, Living Room, Kitchen, Basement")
    print("3. Each Area Has two doors Each leading to another Area")
    print("4. One Room Will have a door leading outside. The door is assigned randomly at the beginning of the game.")
    print("5. The Bathroom Cannot Lead outside. ")
    print("6. You have 7 doors to open before you get caught")
    print("7. Once your lives get to zero the game ends or if you escape\n \n ")

    startgame= input("Would you like to begin the game? (Enter 1 for 'Yes' or 2 for 'No'): \n")

    if startgame == "1":
 
        #List responsible for storing 'Door' objects
        room_doors = []

        #Creats a list of two 'Door' objects tied to each destination in the 'destinations' list.
        #Ensures that only one outside Door object is created.
        for dest in destinations:
            if dest == "Outside":
                room_doors.append(Door(dest))
                continue
            else:
                room_doors.append(Door(dest))
                room_doors.append(Door(dest))

        #Initialize player lives and various rooms. 
        playerLives= 7
        bedroom= Bedroom()
        bathroom= Bathroom()
        livingroom=  LivingRoom()
        kitchen= Kitchen()
        basement= Basement()

        roomList= [bedroom, bathroom, livingroom, kitchen, basement]

        #Allows player to choose th game's difficulty. 
        #Difficulty level will impact the amount of points lost when a special item question is incorrectly answered. 
        penalty = None
        game_difficulty= input("Choose your difficulty. Enter 1 for easy, 2 for medium or 3 for hard: \n")
        
        #Error handling for difficulty setting input.
        while True: 
            try:
                game_difficulty = int(game_difficulty)
                if game_difficulty in (1,2,3):
                    break
                else:
                    raise ValueError
            except ValueError:
                game_difficulty = input("Invalid choice. Enter 1, 2 or 3: \n")

        #Sets penalty based on selected difficulty level
        if game_difficulty == 1:
            penalty = 1
        elif game_difficulty == 2:
            penalty = 2
        elif  game_difficulty == 3:
            penalty = 3

        #Initializes player and assigns a starting room
        playerName= input("Enter player name: \n")
        player1= Player(playerName, random.choice(roomList))

        while playerLives > 0:
            #Display's player location and lists room items
            player1.confirm_location()
            print ("\n")
            print (player1.currentLocation.roomitems())

            #Highlights presence of special item
            search_request= input ("There may be a special item here, do you want to search? (Y or N): \n \n")
            if search_request.lower() == "y":
                print (player1.currentLocation.specialitem())
                room_special= player1.currentLocation.special_item

                #Presents question in order to collect the special item.
                collect_request= input("Woudd you like to collect this item? (Y or N): \n \n" )
                if collect_request.lower() =='y':
                    randomQuestion= random.choice(list(questions.keys()))
                    answer = questions[randomQuestion]
                    quiz= input(randomQuestion + " \n \n")
                    
                    #Checks formatting of answer. Takes away a life if incorrectly inputted.
                    if isinstance(answer, int):
                        try:
                            quiz= int(quiz)
                        except ValueError:
                            print("Incorrect answer format. Life lost!")
                            playerLives -= penalty
                            print(f"{player1.name}, you have {playerLives} lives left. \n \n")
                            if playerLives <= 0:
                                print("You ran out of lives! Game Over.")
                                game_over = True
                                break
                            continue
                    elif isinstance(answer, str):
                        quiz = quiz.lower().strip()
                        answer= answer.lower().strip()
                    
                    #Adds item to player's inventory if correctly answered.
                    #Subtracts a life if incorrectly answered. 
                    if quiz == answer:
                        player1.item_pickup(room_special)
                    else: 
                        print ("Oops. Wrong answer... you lost a life. \n \n")
                        playerLives-= penalty
                        print(f"{player1.name}, you have {playerLives} lives left. \n \n")
                        if playerLives <= 0:
                            print("You ran out of lives! Game Over.\n \n ")
                            game_over = True
                            break
                        pass
            
            #Presents available doors atfer the special item phase is completed. 
            print (f"Door 1: {player1.currentLocation.door1.door_dest()}.\n \n")
            print (f"Door 2: {player1.currentLocation.door2.door_dest()}. \n \n")
            playerMove= input ("Choose your door (1 or 2): \n \n")
            
            #Moves player to the next room based on the door's destination.
            #Ends the game if the chosen door is an outside door. 
            #Otherwise, subtract 1 life.
            if playerMove == "1":
                print ("Moving to the next room...\n \n")
                if player1.currentLocation.door1.dest== "Outside":
                    print ("You escaped! Thanks for playing!")
                    game_over = True
                    break
                else:
                    player1.player_move(player1.currentLocation.door1)
            elif playerMove == "2": 
                print ("Moving to the next room...\n")
                if player1.currentLocation.door2.dest== "Outside":
                    print ("You escaped! Thanks for playing!")
                    game_over = True
                    break
                else:
                    player1.player_move(player1.currentLocation.door2)
            playerLives-=1 
            print(f"{player1.name}, you have {playerLives} lives left. \n \n")
    else:
        game_over = True
            
    ###################### END OF PROGRAM ####################


