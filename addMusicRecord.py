# Add new music record
import pickle
def addMusicRecord():
    myDict = {}
    myList = []
    finalRecord = {}
    musicRecord = open("musicRecord.pkl", 'rb')
    myList = pickle.load(musicRecord)
    musicRecord.close()

    #Finds last auto-generated album unique ID
    if len(myList) == 0:
        lastAlbumUniqueID = 0
    else:
        finalRecord = myList[len(myList)-1]
        lastAlbumUniqueID = finalRecord.get("albumuniqueid", None)+1
    
    myBandArtist = input("Enter the band or artist: ")
    myAlbumTitle = input("Enter the album title: ")
    myYearPublished = input("Enter the year published: ")
    myDuration = input("Enter the duration (in minutes): ")
    myRecordLabel = input("Enter the record label: ")

    myDict["albumuniqueid"] = lastAlbumUniqueID
    myDict["bandartist"] = myBandArtist
    myDict["albumtitle"] = myAlbumTitle
    myDict["yearpublished"] = myYearPublished
    myDict["duration"] = myDuration
    myDict["recordlabel"] = myRecordLabel

    myList.append(myDict)

    musicRecord = open("musicRecord.pkl", 'wb')
    pickle.dump(myList, musicRecord)
    musicRecord.close()
