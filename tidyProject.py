# 0. Prepare for work
# 0.1 Import necessary libraries
import os

# 0.2 Set working folder
workPath = "D:\\temp2\\G80_Residence_Scene\\"

# 0.3 Create function that unravels a folder
def emptyFolder(curPath, newPath) :
    # 1. get file list
    allFiles = os.listdir(curPath)
    # 2. move every file to new location
    for k in range(0, len(allFiles)) :
        os.rename(curPath + "\\" + allFiles[k], newPath + "\\" + allFiles[k])

# 1. Move contents of every subfolder to the main folder
# 1.01 Read subfolders (filter out files)
dirPresent = True

while (dirPresent) :
    dirPresent = False
    allList = os.listdir(workPath)
    dirList = []
    for item in allList :
        if os.path.isdir(workPath + item) :
            dirList.append(item)
            dirPresent = True
# 1.02 Move their content to the main folder
    for i in range(0, len(dirList)):
        movePath = workPath + dirList[i]
        for file in os.listdir(movePath):
            if not os.path.exists(workPath + file) :
                os.rename((movePath + "\\" + file), (workPath + file))
            else :
                emptyFolder((workPath + file), (workPath))
                os.rmdir(workPath + file)
                os.rename((movePath + "\\" + file), (workPath + file))
# 1.03 delete the old subfolders
        os.rmdir(movePath)
# 1.04 Repeat until no more directories

# 2. Sort files to maps and 3d files
# 2.01 Create necessary subfolders if they're not present yet
newFolders = ["maps", "assets"]
for item in newFolders :
        os.mkdir(workPath + item)
# 2.02 Check file extensions and move files accordingly
allList = os.listdir(workPath)
for item in allList :
    ext = (os.path.splitext(item))[1]
    if (ext == ".jpg") or (ext == ".exr") or (ext == ".tif") or (ext == ".png") or (ext == ".tga") or (ext == ".bmp") or (ext == ".hdr") :
        os.rename(workPath + item, workPath + "maps\\" + item)
    elif (ext == ".max") or (ext == ".vrmesh") :
        os.rename(workPath + item, workPath + "assets\\" + item)
