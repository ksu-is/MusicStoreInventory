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

#recordStoreError = "I'm sorry, I don't understand. \n[s] Leave store.\n[1] See all inventory?\n[2] Search by band name?\n"

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

#This is a menu where users get to select albums to purchase or leave the program
def enterStore(greeting = "Hi! Welcome to AJ's Record Store!"):
    print(greeting)
    userSelection = input("Would you like to:\n[s] leave?\n[1] purchase an album?\n")
    if testNumericInput(userSelection):
        purchaseAlbum()
    else:
        enterStore("I'm sorry, I did not understand your response.")

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

#user decides here if they want to purchase an album or look for more
#def purchaseAlbum(purchaseGreeting = "Great!\n[s] Leave store.\n[1] See all inventory?\n[2] Search by band name?"):
    #userSelection = input(purchaseGreeting +"\n")
    #if testNumericInput(userSelection) and int(userSelection) == 1:
        #printStoreInventory()
        #testPurchase()
    #elif testNumericInput(userSelection) and int(userSelection) == 2:
        #bandName = input('Great, enter a band name:\n')
        #if bandName.isalpha():
            #printStoreInventory()
        #else:
            #purchaseAlbum(recordStoreError)
    #else:
        #purchaseAlbum(recordStoreError)

#user can withdraw more money from a bank
def enterBank():
    print("Your balance is: " + str(player['cash']))
    userSelection = input("How much would you like to withdraw? No withdraws less than $5.\n")
    if testNumericInput(userSelection) and float(userSelection) > 4:
        player['cash'] += float(userSelection)
        print("Your balance is: " + str(player['cash']))
        enterStreet()
    else:
        print("I'm sorry, I don't understand")
        enterBank()

#after creating a player, users see this menu with 3 options
#the user will be able to enter the bank, enter the store, or exit the game
def enterStreet():
    print('street entered')
    userSelection = input("[1] - Enter Bank\n[2] - Enter record store.\n[e] - Exit application.\n")
    if testNumericInput(userSelection) and int(userSelection) == 1:
        enterBank()
    elif testNumericInput(userSelection) and int(userSelection) == 2:
        enterStore()
    else:
        print("I'm sorry, I don't understand")
        enterStreet()

    
initGame()