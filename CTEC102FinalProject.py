import time #imported a time module to add a delay between some printed statements

DELAY = 1 #delay variable to be able to set the in one spot


class Room:  #A class definition named Room.
  def __init__(self, name, color, hints): #An _ _init_ _ method for the class. The method accepts an argument for each of the data attributes.
      self.name = name #attributes for the room’s name.
      self.color = color #attributes for the room’s color.
      self.hints = hints #attributes for the room’s hints that I don't even end up using .

#Mutator methods for each data attribute.
  def set_name(self, name):
      self.name = name
  def set_color(self, color):
      self.color = color
  def set_hints(self, hints):
      self.hintss = hints

#Accessor methods for each data attribute.
  def get_name(self):
      return self.name
  def get_color(self):
      return self.color
  def get_hints(self):
      return self.hints

#An _ _str_ _ method that returns a string indicating the state of the object.
  def __str__(self):
      return f"{self.name}{self.color}{self.hints}"

#creating each room object and setting the values for their attributes
Top = Room('top', 'white', 'cube')
North = Room('north', 'blue', 'hints')
West = Room('west', 'red', 'hints')
Middle = Room('middle', 'black', 'Directions')
East = Room('east', 'orange', 'hints')
South = Room('south', 'green', 'hints')
Bottom = Room('bottom', 'yellow', 'Place Box')

#I named the game cube game and it's got three main parts start, middle and end
def cube_game():
    #I defined a function to make a beginning to the game. 
    def start_game():

        print(f"You're in a room with a {Top.color} floor.")# A function string pulling an attribute from a book object
        time.sleep(DELAY) #delay to keep every line from printing at once
        
        print(f"There's a {Top.hints} about 2.5 inches tall in the middle of it.")# A function string pulling an attribute from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        #assigned a a boolean to a variable to continue the loop until the user says yes
        cube_possession = False #False value assigned to the cube_possession variable
        while cube_possession == False: #while loop that remains true until the cube_possession variable changes in the if statement
            answer = input("Do you pick up the cube?: ") #prompts the user to reply and stores the answer in the answer variable
            if answer.lower() == "yes": #takes the value of the answer variable, makes it all lowercase and compaires it to yes
                print("You hear a click") #if lowercase version of answer value is yes, will print this string, and do the the next line
                cube_possession = True #sets the cube_possession value to true
            elif answer.lower() == "no": #takes lowercased answer value and compaires it to no 
                print("Serisouly! This could take a while") #if lowercase version of answer value is no, will print this string, and go the the next line
            else: #if the top two conditions are false it will default to else
                print("Invalid Answer") #displays print statemant
                print("Please respond: yes or no") #lets user know what the valid answers are

        print("The floor opens up and drops you to the room below.") #the last print statement that's executed after the while loop

    start_game() #calling the start_game function



    def middle_room(): #defined a function named middle_room with the main pard of the game in it
        #Display test to set the scene of the game
        print('You feel the box changing shape in you hands.') 
        time.sleep(DELAY)#delay to keep every line from printing at once
        print("It's divided itself into even sections")
        time.sleep(DELAY)#delay to keep every line from printing at once
        print('You feel the box wants in the four rooms around you')
        time.sleep(DELAY)#delay to keep every line from printing at once

        #I set accumulators and values for attributes to be used for loops, and conditions
        ALL_ROOMS = 6 #set this variable to use with the main while loop so the loop will end rooms_explored variable is no longer less than six
        rooms_explored = 2 #you'll only explore four rooms in this section and each time they add to the rooms_explored accumulator
        north_explored = 0 #set this accumulator to zero and it will be added to after the north room is explored
        east_explored = 0 #set this accumulator to zero and it will be added to after the east room is explored
        south_explored = 0 #set this accumulator to zero and it will be added to after the south room is explored
        west_explored = 0 #set this accumulator to zero and it will be added to after the west room is explored
        north_room_explored = False #initialized the variable with a false value to start the while condition and to change it after the variable value is changed
        east_room_explored = False #initialized the variable with a false value to start the while condition and to change it after the variable value is changed
        south_room_explored = False #initialized the variable with a false value to start the while condition and to change it after the variable value is changed
        west_room_explored = False #initialized the variable with a false value to start the while condition and to change it after the variable value is changed
        global tokens #uesd global keyword to open the scope of the variable
        tokens = 0 #i needed more items for the assignment but I didn't want to disturb the flow
        #main while loop that makes you visit each room but can't enter any room twice.
        while rooms_explored < ALL_ROOMS: #while loop that continues until all rooms in the middle are visited.
            rooms_choice = input('Which room will you enter? North  East  South  West: ') #prompts user for the room they want to enter first
            if rooms_choice.lower() == 'north' and north_explored == 0: #condition that takes the user responce and if room had been explored
                print(f"You're in {North.name} room, the south wall is {North.color}, and you hear the door lock behind you.")# A function string pulling attributes from a book object
                #nested while loop to have choices in the game. changes the boolean value of north_room_explored when the correct answer is given.
                while north_room_explored == False: #while loop yo continue to prompt user until the correct answer is given
                    north_room_choice = input("What are you going to do now? \nA) Try to open the door \nB) Shake the cube \nC) Ask the cube what it wants\n   Choose from number A, B, or C:") #prompts user with three different options
                    if north_room_choice.upper() == "A": #checks the uppercase version of user responce it equal to A
                        print("The door won't open") #displayed statement if user responce is equal to A
                    elif north_room_choice.upper() == "B": #checks the uppercase version of user responce it equal to B
                        print("The cube gets angry") #displayed statement if user responce is equal to B
                    elif north_room_choice.upper() == "C": #checks the uppercase version of user responce it equal to C
                        north_room_explored = True #The correct responce breaks the while loop
                        tokens += 1 #added a token to have more items in the game
                        print(f"You have {tokens} tokens")#print statement to keep up with the tokens
                        print("You received a token for the room") #Lets user know they got a token
                    else: #default if no conditions are met
                        print("Invalid responce. Please enter A, B, or C: ") #Displayed statement for the default else
                #print statements after the rooms while loop is broken and adds to two accumulators  
                print(f"The cube wants to touch the 9 square hieroglyphic with the {North.color} paint in the {North.name} room")# A function string pulling attributes from a book object
                print(f"You go back to the {Middle.name} room")# A function string pulling an attribute from a book object
                rooms_explored += 1 #adds one to the rooms_explored accumulator this is to eventually complete exploring all the rooms.
                north_explored += 1 #adds ont to the north_explored accumulator to work with the main if statement of this room. keeps you from entering the same room twice
            #condition to check the user input and the east_explored accumulator, also prompts user for options in the room
            elif rooms_choice.lower() == 'east' and east_explored == 0: #condition that takes the user responce and if room had been explored
                print(f"You're in {East.name} room, the west wall is {East.color}, and you hear the door lock behind you")# A function string pulling attributes from a book object
                #nested while loop to have choices in the game. changes the boolean value of east_room_explored when the correct answer is given.
                while east_room_explored == False: #while loop yo continue to prompt user until the correct answer is given
                    east_room_choice = input("What are you going to do now? \nA) Yell for help \nB) Listen to the cube \nC) Put the cube down \n   Choose from number A, B, or C:") #prompts user with three different options
                    if east_room_choice.upper() == "A": #checks the uppercase version of user responce it equal to A
                        print("All you hear is your echo") #displayed statement if user responce is equal to A
                    elif east_room_choice.upper() == "B": #checks the uppercase version of user responce it equal to B
                        east_room_explored = True #The correct responce breaks the while loop
                        tokens += 1 #added a token to have more items in the game
                        print(f"You have {tokens} tokens")#print statement to keep up with the tokens
                        print("You received a token for the room") #Lets user know they got a token
                    elif east_room_choice.upper() == "C": #checks the uppercase version of user responce it equal to C
                        print("The cube gets upset so you pick it back up") #displayed statement if user responce is equal to C
                    else: #default if no conditions are met
                        print("Invalid responce. Please enter A, B, or C: ") #Displayed statement for the default else
                #print statements after the rooms while loop is broken and adds to two accumulators 
                print(f"The cube wants to touch the 9 square hieroglyphic with the {East.color} paint in the {East.name} room")# A function string pulling attributes from a book object
                print(f"You go back to the {Middle.name} room")# A function string pulling an attribute from a book object
                rooms_explored += 1 #adds one to the rooms_explored accumulator this is to eventually complete exploring all the rooms.
                east_explored += 1 #adds ont to the east_explored accumulator to work with the main if statement of this room. keeps you from entering the same room twice
            #condition to check the user input and the south_explored accumulator, also prompts user for options in the room
            elif rooms_choice.lower() == 'south' and south_explored == 0: #condition that takes the user responce and if room had been explored
                print(f"You're in {South.name} room, the north wall is {South.color}, and you hear the door lock behind you")# A function string pulling attributes from a book object
                #nested while loop to have choices in the game. changes the boolean value of south_room_explored when the correct answer is given.
                while south_room_explored == False: #while loop yo continue to prompt user until the correct answer is given
                    south_room_choice = input("What are you going to do now? \nA) Do what the cube wants \nB) Open the door \nC) Explore a bit\n   Choose from number A, B, or C:") #prompts user with three different options
                    if south_room_choice.upper() == "A": #checks the uppercase version of user responce it equal to A
                        south_room_explored = True #The correct responce breaks the while loop
                        tokens += 1 #added a token to have more items in the game
                        print(f"You have {tokens} tokens")#print statement to keep up with the tokens
                        print("You received a token for the room") #Lets user know they got a token
                    elif south_room_choice.upper() == "B": #checks the uppercase version of user responce it equal to B
                        print("The door won't open") #displayed statement if user responce is equal to B.
                    elif south_room_choice.upper() == "C": #checks the uppercase version of user responce it equal to C
                        print("There's nothing in here") #displayed statement if user responce is equal to C.
                    else: #default if no conditions are met
                        print("Invalid responce. Please enter A, B, or C: ") #Displayed statement for the default else
                #print statements after the rooms while loop is broken and adds to two accumulators 
                print(f"The cube wants to touch the 9 square hieroglyphic with the {South.color} paint in the {South.name} room")# A function string pulling attributes from a book object
                print(f"You go back to the {Middle.name} room")# A function string pulling an attribute from a book object
                rooms_explored += 1 #adds one to the rooms_explored accumulator this is to eventually complete exploring all the rooms.
                south_explored += 1 #adds ont to the south_explored accumulator to work with the main if statement of this room. keeps you from entering the same room twice
            #condition to check the user input and the west_explored accumulator, also prompts user for options in the room
            elif rooms_choice.lower() == 'west' and west_explored == 0: #condition that takes the user responce and if room had been explored
                print(f"You're in {West.name} room, the east wall is {West.color}, and you hear the door lock behind you")# A function string pulling attributes from a book object
                #nested while loop to have choices in the game. changes the boolean value of west_room_explored when the correct answer is given.
                while west_room_explored == False: #while loop yo continue to prompt user until the correct answer is given
                    west_room_choice = input("What are you going to do now? \nA) Find a way out \nB) Examine the cube \nC) Ask the cube what it wants\n   Choose from number A, B, or C:") #prompts user with three different options
                    if west_room_choice.upper() == "A": #checks the uppercase version of user responce it equal to A
                        print("There's no way out") #displayed statement if user responce is equal to A.
                    elif west_room_choice.upper() == "B": #checks the uppercase version of user responce it equal to B
                        print("Just a block, but you think there's more to it") #displayed statement if user responce is equal to B.
                    elif west_room_choice.upper() == "C": #checks the uppercase version of user responce it equal to C
                        west_room_explored = True #The correct responce breaks the while loop
                        tokens += 1 #added a token to have more items in the game
                        print(f"You have {tokens} tokens") #print statement to keep up with the tokens
                        print("You received a token for the room") #Lets user know they got a token
                    else: #default if no conditions are met
                        print("Invalid responce. Please enter A, B, or C: ") #Displayed statement for the default else
                #print statements after the rooms while loop is broken and adds to two accumulators 
                print(f"The cube wants to touch the 9 square hieroglyphic with the {West.color} paint in the {West.name} room")# A function string pulling attributes from a book object
                print(f"You go back to the {Middle.name} room")# A function string pulling an attribute from a book object
                rooms_explored += 1 #adds one to the rooms_explored accumulator this is to eventually complete exploring all the rooms.
                west_explored += 1 #adds ont to the west_explored accumulator to work with the main if statement of this room. keeps you from entering the same room twice

            elif rooms_choice.lower() == 'north' and north_explored == 1: #privides the option for if the room has been explored already
                print(f"The cube doesn't want to enter the {North.name} room again!")# A function string pulling an attribute from a book object

            elif rooms_choice.lower() == 'east' and east_explored == 1: #privides the option for if the room has been explored already
                print(f"The cube doesn't want to enter the {East.name} room again!")# A function string pulling an attribute from a book object

            elif rooms_choice.lower() == 'south' and south_explored == 1: #privides the option for if the room has been explored already
                print(f"The cube doesn't want to enter the {South.name} room again!")# A function string pulling an attribute from a book object

            elif rooms_choice.lower() == 'west' and west_explored == 1: #privides the option for if the room has been explored already
                print(f"The cube doesn't want to enter the {West.name} room again!")# A function string pulling an attribute from a book object

            else: #default statement for responces that don't match preferred input
                print("That wasn't an option!") #default statemant for the main if elif else statemant
                time.sleep(DELAY) #delay to keep every line from printing at once
                print(f"The choices are {North.name}, {East.name}, {South.name}, or {West.name}.")# A function string pulling attributes from a book object
    middle_room() #calls the the middle_room function
    #created the third function that ends the game
    def bottom_room(): #defined the third function bottom_room
        print("Once again, the floor opens up. You fall with the cube in your hands") #displayed statement to start the final area
        time.sleep(DELAY)#delay to keep every line from printing at once
        print(f"The ceiling is {Bottom.color}, and you're starting to put everything together")# A function string pulling an attribute from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        print(f"The floor of the first room was {Top.color}")# A function string pulling an attribute from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        print(f"The wall of the {North.name} room was {North.color}")# A function string pulling attributes from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        print(f"The wall of the {South.name} room was {South.color}")# A function string pulling attributes from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        print(f"The wall of the {East.name} room was {East.color}")# A function string pulling attributes from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        print(f"The wall of the {West.name} room was {West.color}")# A function string pulling attributes from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        print(f"Now the ceiling of the {Bottom.name} room is {Bottom.color}")# A function string pulling attributes from a book object
        time.sleep(DELAY)#delay to keep every line from printing at once
        print("As you think about the different colors, and their placement.") #displayed statement to wrap up the game
        print("The same colors start appearing on the cube ") #displayed statement to wrap up the game
        correct_guess = False #set a initializer to False to use in a while loop
        while correct_guess == False: # while correct_guess is false the loop will continue
            inventor_name = input("What's the inventor of the cube's last name?") #prompt user to guess a last name
            if inventor_name.lower() == "rubik": #takes the value of the user's responce, changes it to lowercase, and comapires it to rubik
                correct_guess = True #changes the correct guess value to True and stops the while loop
                print("The cube is excited") #display statemant
                time.sleep(DELAY)#delay to keep every line from printing at once
                print("You're almost outta there") #display statemant
                time.sleep(DELAY)#delay to keep every line from printing at once
                print("What are you gonna do with the tokens?")#display statemant
                time.sleep(DELAY)#delay to keep every line from printing at once
                print("There's a mantel with four empty places.") #a print statement for narrative 
                won_game = False #made a variable and set the value to false for a while loop later
                while tokens == 4 and won_game == False: #while loop that compaires the value of tokens and won_game variable
                    place_token = input("Place tokens on the mantel?: ") #prompt user for input
                    if place_token.lower() == "yes": #condition to compair the user input to yes
                        print("A loud voice says, sometimes you gotta do what you gotta do to complete the assignment!") #display statemant  
                        print("Congratulations! You win the game.") #Displays a statement that you've won the game
                        won_game = True #changes the value of the won_game variable to True to kill the while loop
                    elif place_token.lower() == "no": #another option to yes
                        print("Not much is gonna happen until you do.") #display statement if the no condition is true
                    else:#default option
                        print("Just say yes") #making it easy for the user
                
            elif inventor_name.lower() == "hint": #takes the value of the user's responce, changes it to lowercase, and comapires it to hint
                print("Erno Rubik invented the Rubik's Cube") #displays a hint if user ask for a hint
            elif inventor_name.lower() == "better hint": #takes the value of the user's responce, changes it to lowercase, and comapires it to better hint
                print("It's Rubik. The answer is Rubik") #displays the answer
            else: #default else statement
                print("Invalid answer, but try responding with hint or better hint.") #default statement that prompts you to ask for a hint.
    bottom_room() #calls the third nested function
cube_game() #calls the main function
