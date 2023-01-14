# view music records

import pickle
def viewMusicRecords():
    myList = []
    musicRecord = open('musicRecord.pkl','rb')
    myList = pickle.load(musicRecord)
    musicRecord.close()

    for item in myList:
        print("Album ID: ", item['albumuniqueid'])
        print("Band or Artist: ", item['bandartist'])
        print("Album Title: ", item['albumtitle'])
        print("Year Published: ", item['yearpublished'])
        print("Duration: ", item['duration'])
        print("Record Label: ", item['recordlabel'])
        print()
        
