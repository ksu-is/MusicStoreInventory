#creating empty player for createPlayer()
player = {'name':'', 'cash':0, 'inventory':[]}

#I added some of my favorite bands into the inventory 
storeInventory = [
    {'name':'Moving Pictures','band':'Rush','cost':14.99},
    {'name':'Power Windows','band':'Rush','cost':12.99},
    {'name':'Invisible Touch','band':'Genesis','cost':10.50},
    {'name':'Emperor of Sand','band':'Mastodon','cost':13.75},
    {'name':'Hushed and Grim','band':'Mastodon','cost':11.99},
    {'name':'Hurley','band':'Weezer','cost':12.50}
          ]

#initGame() will be called later to start the shop
def initGame():
    createPlayer()
    enterStreet()

#This is the first menu the player will see
#This is mainly for fun so you can enter any amount of money  
def createPlayer():
    player['name'] = input("What is your name?\n")
    player['cash'] = input("How much money do you have?\n")
    while(testNumericInput(player['cash']) == False):
        player['cash'] = input("I'm sorry, please answer with a number. How much money do you have?\n")
    player['cash'] = float(player['cash'])

#after creating a player, users see this menu with 3 options
#the user will be able to enter the bank, enter the store, or exit the game
#i will create enterbank() and enterStore() later but this is where they will be called
def enterStreet():
    print('street entered')
    #userSelection = input("[1] - Enter Bank\n[2] - Enter record store.\n[e] - Exit application.\n")
    #if testNumericInput(userSelection) and int(userSelection) == 1:
        #enterBank()
    #elif testNumericInput(userSelection) and int(userSelection) == 2:
        #enterStore()
    #else:
        #print("I'm sorry, I don't understand")
        #enterStreet()

#determines if user input is a number that will be used in menus or exits the game or returns the street if given the right character
def testNumericInput(usrInput):
    if usrInput == "e":
        exit()
    elif usrInput == "s":
        enterStreet()
    elif usrInput.isdigit() == True:
        return True
    else:
        return False
    
initGame()