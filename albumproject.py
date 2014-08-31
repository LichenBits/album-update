#!/usr/bin/python2
import os
import musicbrainzngs as mb
import beets

mb.set_useragent('artistupdate', 1.0)
artistList = []
localList = []
brainzList = {}
mbList = []
homeDir = os.environ['HOME']
lib = beets.Library(path=homeDir + '/.config/beets/library.db')


def getMBID():
    for artists in lib.albums():
        if len(artists['mb_albumartistid']) == 0:
            pass
        else:
            artistList.append(artists['mb_albumartistid'])
            # localList.append(artists['mb_albumid'])
            localList.append(artists['album'])
    for albums in set(artistList):
        # online album db
        brainzList.update(mb.browse_release_groups(artist=albums))
    for info in brainzList['release-group-list']:
        mbList.append(info['title'])

    # def compare():
    for mbid in mbList:
        if mbid in localList:
            pass
        else:
            print mbid

if __name__ == '__main__':
    getMBID()
