# Search Music Records
import pickle
def searchMusicRecords():
    print("Search Music Records Menu")
    print("1. By Album Unique ID")
    print("2. By Band or Artist")
    print("3. By Album Title")
    print("4. By Year Published")
    print("5. By Record Label")

    mySearchInput = int(input("Enter a choice (1-5): "))
    count = 0
    myList = []
    musicRecord = open('musicRecord.pkl','rb')
    myList = pickle.load(musicRecord)
    musicRecord.close()

    if mySearchInput == 1:
        myUniqueAlbumIDInput = int(input("Enter a unique album ID: "))
        for i in range(0,len(myList)):
            for k,v in myList[i].items():
                if v == myUniqueAlbumIDInput:
                    count += 1
                    print("Band Name: ", myList[i].get("bandartist"))
                    print("Album Title Name: ", myList[i].get("albumtitle"))
                    print("Year Published: ", myList[i].get("yearpublished"))
                    print("Duration: ", myList[i].get("duration"))
                    print("Record Label:", myList[i].get("recordlabel"))
        if count == 0:
            print("Music Record Not Found!")
            
    if mySearchInput == 2:
        myBandArtistInput = input("Enter a band or artist: ")
        for i in range(0,len(myList)):
            for k,v in myList[i].items():
                if v == myBandArtistInput:
                    count += 1
                    print("Band Name: ", myList[i].get("bandartist"))
                    print("Album Title Name: ", myList[i].get("albumtitle"))
                    print("Year Published: ", myList[i].get("yearpublished"))
                    print("Duration: ", myList[i].get("duration"))
                    print("Record Label:", myList[i].get("recordlabel"))
        if count == 0:
            print("Music Record Not Found!")
        
    elif mySearchInput == 3:
        myAlbumTitleInput = input("Enter the album title: ")
        for i in range(0,len(myList)):
            for k,v in myList[i].items():
                if v == myAlbumTitleInput:
                    count += 1
                    print("Band Name: ", myList[i].get("bandartist"))
                    print("Album Title Name: ", myList[i].get("albumtitle"))
                    print("Year Published: ", myList[i].get("yearpublished"))
                    print("Duration: ",myList[i].get("duration"))
                    print("Record Label:",myList[i].get("recordlabel"))
        if count == 0:
            print("Music Record Not Found!")
            
    elif mySearchInput == 4:
        myYearPublishedInput = input("Enter the year published: ")
        for i in range(0,len(myList)):
            for k,v in myList[i].items():
                if v == myYearPublishedInput:
                    count += 1
                    print("Band Name: ", myList[i].get("bandartist"))
                    print("Album Title Name: ", myList[i].get("albumtitle"))
                    print("Year Published: ", myList[i].get("yearpublished"))
                    print("Duration: ", myList[i].get("duration"))
                    print("Record Label:", myList[i].get("recordlabel"))
        if count == 0:
            print("Music Record Not Found!")
            
    elif mySearchInput == 5:
        myRecordLabelInput = input("Enter the record label: ")
        for i in range(0,len(myList)):
            for k,v in myList[i].items():
                if v == myRecordLabelInput:
                    count += 1
                    print("Band Name: ",myList[i].get("bandartist"))
                    print("Album Title Name: ",myList[i].get("albumtitle"))
                    print("Year Published: ",myList[i].get("yearpublished"))
                    print("Duration: ",myList[i].get("duration"))
                    print("Record Label:", myList[i].get("recordlabel"))
        if count == 0:
            print("Music Record Not Found!")
