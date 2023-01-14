import pickle
# Change music records
def changeMusicRecords():
    count =0
    myList = []
    myDict = {}
    musicRecord = open('musicRecord.pkl','rb')
    myList = pickle.load(musicRecord)
    musicRecord.close()

    myBandInput = input("Enter a band or artist name: ")
    myAlbumTitleInput = input("Enter an album title: ")

    for i in range(0, len(myList)):
        for k,v in myList[i].items():
            if v == myBandInput:
                count += 1
                myAlbumTitle = myList[i].get("albumtitle")
                if myAlbumTitle == myAlbumTitleInput:
                    print("Record Information")
                    print("Band/Artist: ", myBandInput)
                    print("Album Title: ",myAlbumTitle)
                    print("Year Published: ",myList[i].get("yearpublished"))
                    print("Record Duration: ", myList[i].get("duration"))
                    print("Record Label Name: ", myList[i].get("recordlabel"))

                    print("Which item in the record would you like to change?")
                    print("Menu Selection")
                    print("1. Year Published")
                    print("2. Duration")
                    print("3. Record Label")
                    
                    myMenuSelectionInput = int(input("Enter a menu selection: "))

                    if myMenuSelectionInput == 1:
                        newYearPublishedInput = input("Enter the new year published: ")
                        myList[i]["yearpublished"] = newYearPublishedInput

                    elif myMenuSelectionInput == 2:
                        newDurationInput = input("Enter the new record duration: ")
                        myList[i]["duration"] = newDurationInput
                        
                    elif myMenuSelectionInput == 3:
                        newRecordLabelInput = input("Enter the new record label: ")
                        myList[i]["recordlabel"] = newRecordLabelInput

                    musicRecord = open('musicRecord.pkl','wb')
                    pickle.dump(myList,musicRecord)
                    musicRecord.close()
    if count == 0:
        print("Music Record not found!")
