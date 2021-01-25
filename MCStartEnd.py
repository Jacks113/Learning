from zipfile import ZipFile
import os
from os.path import basename
from subprocess import call


with ZipFile('server spigot 1.16.4.zip', 'r') as file:
    file.extractall()

call('server\serverrun.bat')
#call('server\ ngrok.exe')


dirName = "server"


# create a ZipFile object
with ZipFile('MCServer.zip', 'w') as zipObj:
    # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk(dirName):
        for filename in filenames:
            # create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            # Add file to zip
            zipObj.write(filePath)

    #zipObj.write('McStartend.exe')


