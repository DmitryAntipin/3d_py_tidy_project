#import stuff
import os
#set working folder
workPath = "" #Enter the project folder here (remember double slashes \\ ) !

#function for moving files - if an item is a file, it will move it to top level working folder.
def scavengeFiles(source, destination) :
    allItems = os.listdir(source)
    for i in range (0, len(allItems)) :
        if (not os.path.isdir(source + "\\" + allItems[i])) :
            os.rename(source + "\\" + allItems[i], destination + "\\" + allItems[i])
        else :
            scavengeFiles(source + "\\" + allItems[i], workPath)

#function for filtering out folders - returns a list of folders in a folder (excludes files)
def filterFolders(source) :
    allList = os.listdir(source)
    dirList = []
    for item in allList:
        if os.path.isdir(source + "\\" + item):
            dirList.append(item)
    return dirList

#function for removing all the empty folders - deletes a folder if it's empty and looks lower into subfolders if it's not
def killFolders(source) :
    dirList = filterFolders(source)
    while (len(dirList) > 0) :
        for item in dirList :
            if len(os.listdir(source + "\\" + item)) == 0 :
                os.rmdir((source + "\\" + item))
            else :
                killFolders(source + "\\" + item)
        dirList = filterFolders(source)

#function for sorting out the files - checks file extensions and sorts the files either as maps or assets
def sort3Dfiles(source) :
    newFolders = ["maps", "assets"]
    for item in newFolders:
        os.mkdir(source + "\\" + item)
    allList = os.listdir(source)
    for item in allList:
        ext = (os.path.splitext(item))[1]
        if (ext == ".jpg") or (ext == ".JPG") or (ext == ".exr") or (ext == ".EXR") or (ext == ".tif") or (ext == ".TIF") or (ext == ".png") or (ext == ".PNG") or (ext == ".tga") or (ext == ".TGA") or (ext == ".bmp") or (ext == ".BMP") or (ext == ".hdr") or (ext == ".HDR"):
            os.rename(source + "\\" + item, source + "\\maps\\" + item)
        elif (ext == ".max") or (ext == ".vrmesh"):
            os.rename(source + "\\" + item, source + "\\assets\\" + item)

scavengeFiles(workPath, workPath)
killFolders(workPath)
sort3Dfiles(workPath)