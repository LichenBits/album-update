import musicbrainzngs as mb
import beets

mb.set_useragent('artistupdate', 1.0)
artistList = []
localList = []
brainzList = {}
mbList = []
lib = beets.Library(path='/home/bubber/.config/beets/library.db')

def getMBID(): 
    for artists in lib.albums():
        if len(artists['mb_albumartistid']) == 0:
            pass
        else:
            artistList.append(artists['mb_albumartistid'])
            #localList.append(artists['mb_albumid'])
            localList.append(artists['album'])
    for albums in set(artistList):
        brainzList.update(mb.browse_release_groups(artist=albums)) #online album db
    for info in brainzList['release-group-list']:
        mbList.append(info['title'])

    #def compare():
    for mbid in mbList:
         if mbid in localList:
             pass
         else:
            print mbid
