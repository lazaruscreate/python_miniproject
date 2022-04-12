#!/usr/bin/python3
import os
import time
  

def showStatus():
  #print a main menu and the commands
  # clear the screen after each turn
  os.system("cls")
  print('''
          .-. .-.,---.  ,'|"\  ,---.  ,---.             .--. .-. .-.  .---.,-..---. .-. .-.        .-.   .-. .---. _______,---.  ,---. .-.   .-.  
|\    /|| | | || .-.\ | |\ \ | .-'  | .-.\   |\    /|/ /\ \|  \| | ( .-._)(/ .-. )|  \| | |\    /|\ \_/ )/( .-._)__   __| .-'  | .-.\ \ \_/ )/  
|(\  / || | | || `-'/ | | \ \| `-.  | `-'/   |(\  / / /__\ \   | |(_) \  (_) | |(_)   | | |(\  / | \   (_|_) \    )| |  | `-.  | `-'/  \   (_)  
(_)\/  || | | ||   (  | |  \ \ .-'  |   (    (_)\/  |  __  | |\  |_  \ \ | | | | || |\  | (_)\/  |  ) (  _  \ \  (_) |  | .-'  |   (    ) (     
| \  / || `-')|| |\ \ /(|`-' /  `--.| |\ \   | \  / | |  |)| | |)( `-'  )| \ `-' /| | |)| | \  / |  | | ( `-'  )   | |  |  `--.| |\ \   | |     
| |\/| |`---(_)|_| \)(__)`--'/( __.'|_| \)\  | |\/| |_|  (_)(  (_)`----' `-')---' /(  (_) | |\/| | /(_|  `----'    `-'  /( __.'|_| \)\ /(_|     
'-'  '-'           (__)     (__)        (__) '-'  '-'     (__)             (_)   (__)     '-'  '-'(__)                 (__)        (__|__)  
  ========================================================================================================================================
  Commands:
  go [direction]
  get [item]
  ''')
  
  
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom) 
  # Print the Room Description
  if 'desc' in rooms[currentRoom]:
    print(rooms[currentRoom]['desc'])
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Lobby' : {
                  'east'  : 'Dining Room',
                  'north' : 'Library',
                  'south' : 'Bedroom',
                  'desc'  : 'The foyer of the large home is dusty and dimly lit. You feel an instant feeling of dread overcome you. '

                },
            'Bedroom' : {
                  'north' : 'Lobby',
                  'item'  : 'weapon',
                  'desc'  : 'The bedroom has a foul stench, and you see a bloody knife in what appears to be a dried puddle of blood'
                },
            'Library' : {
                  'south' : 'Lobby',
                  'west'  : 'Study',
                  'desc'  : 'In the old library you see that there are multiple books that have been untouched. To the left of you, you spot a door leading to a study...'
                },
            'Study' : {
                  'east'  : 'Library',
                  'item'  : 'scroll',
                  'desc'  : 'In study you do not see much, but a old scroll titled "My confession" enclosed in locks. What do you do?'
                },
            'Gate' : {
                  'north' : 'Maze'
                },
            'Dining Room' : {
                  'west' : 'Lobby',
                  'south': 'Garden',
                  'desc'  : 'In the kitchen you find things are pristine...almost. There are slighty muddy boot prints leading south to the garden.'                 
                },
            'Garden' : {
                  'north' : 'Dining Room',
                  'east'  : 'Maze',
                  'desc'  : 'The garden is ominous. It feels like a chasm between the mansion, which radiates dark energy, and the void that is the maze to your right. Proceed with Caution.'
                },
            'Maze' : {
                  'north' : 'Shed',
                  'south' : 'Gate',
                  'desc'  : 'As you walk around, getting increasingly disoriented, you are not sure which way is which, but you know one thing: you need to escape NOW.'
                },
            'Shed' : {
                  'south' : 'Maze',
                  'item' : 'killer',
                }
         }

#start the player in the Lobby every game
currentRoom = 'Lobby'

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]     
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] != 'scroll':
      #add the item to their inventory
      inventory += [move[1]]      
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    # This will be the riddle logic. if you pass the first riddle then you get to open the 
    elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] == 'scroll':
      print("You go to grab the scroll, and there are two heavy letter cypher locks with sentences on them..")
      riddle = input("The more of this there is, the less you see. What is it? ")
      # this is the first riddle logic, you cannot access the second riddle if you don't get the first correct
      if riddle.lower() == 'darkness':
        print("\nYou hear a loud click, and one of the two locks disintegrates and leaves one remaining...")
        riddle_two = input("What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps? ")
        #This is the second riddle, if it is correct then you get the confession scroll added to your inventory and can continue
        if riddle_two.lower() == 'river':
          print("The final lock shatters at your correct guess. You read the parchment and see the confession of the grisly murder")
          time.sleep(3.5)
          #add the item to their inventory
          inventory += [move[1]]      
          #display a helpful message
          print(move[1] + ' got!')
          #delete the item from the room
          del rooms[currentRoom]['item']
        else:
          print("Disgruntled, and in even more danger than before, you realize that you will never solve this murder. YOU LOSE")
          time.sleep(3.5)
          break
      else:
        print("Disgruntled, and in even more danger than before, you realize that you will never solve this murder. YOU LOSE")
        time.sleep(3.5)
        break
        
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
    
      

  ## Define how a player can win
  if currentRoom == 'Gate' and 'scroll' in inventory and 'weapon' in inventory:
    print('As you saunter out of the foggy maze, you see a silhouette staring at you, knowing that you know the truth and will bring them to justice. YOU WIN')
    break

  ## The Murderer is who we must avoid, for now we will place them in a room and if you are caught in the same room as them then you are killed
  elif 'item' in rooms[currentRoom] and 'killer' in rooms[currentRoom]['item']:
    print('Out of breath and sweaty, you realize you are now cornered by the looming figure. In your final breaths, you realize your fatal error. YOU LOSE')
    break

