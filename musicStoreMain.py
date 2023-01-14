import searchMusicRecords
import addMusicRecord
import changeMusicRecords
import viewMusicRecords
import sys

def main():
    print("Welcome to the Music Store Inventory")
    #Move to the Main Menu
    MainMenu()

def MainMenu():
    #Printing main menu
    print("***Main Menu***")
    print("1. Search for Music Records")
    print("2. Add new Music Records")
    print("3. Change Music Record information")
    print("4. View All Music Records")
    print("5. Exit Main Menu")

    menuSelectionInput = int(input("Enter a choice (1-5): "))

    if menuSelectionInput == 1:
        searchMusicRecords.searchMusicRecords()
        print()
        MainMenu()
    elif menuSelectionInput == 2:
        addMusicRecord.addMusicRecord()
        MainMenu()
    elif menuSelectionInput == 3:
        changeMusicRecords.changeMusicRecords()
        MainMenu()
    elif menuSelectionInput == 4:
        viewMusicRecords.viewMusicRecords()
        MainMenu()
    elif menuSelectionInput == 5:
        sys.exit("Thank you for using the Music Inventory application. Goodbye!")
    else:
        MainMenu()

if __name__ == "__main__":
    main()
