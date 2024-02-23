import glob, os, zipfile, re, shutil, sys
from os import walk
import pathlib

#
#This works by running the python file in the same directory as the zip folder from Elvis
#

#Set the directory to where the current py file is
path = os.path.dirname(os.path.abspath('__file__'))
path = path.replace(os.sep, '/')

#Figure out where the zip folder is
zipName = ''
for z in os.listdir(path):
    if z[-4:] == '.zip':
        zipName = '/' + z
        break
if zipName == '':
    print("Bro there is no zip folder")

#Extract the zip folder
with zipfile.ZipFile(path+zipName,"r") as zip_ref:
    zip_ref.extractall("FilesExtract")

#Ok now look around in the extracted folder for nested zip folders
archives = os.listdir(path)
archives = [ar for ar in archives if ar.endswith(".zip")]
for a in archives:
    archive = zipfile.ZipFile( path+'\\'+a )
    filelist = archive.namelist()
    
#Check that they're actually zip folders
ziplist = []
for b in filelist:
    if (b[-4:]) == '.zip':
       ziplist.append(b)
       
#Extract all the nested zip folders into a temp folder
count = 0
for c in ziplist:
    count = count + 1
    with zipfile.ZipFile(path + '/FilesExtract/' + c,"r") as zip_ref:
        zip_ref.extractall("SubFiles/Extract"+str(count))

#Set up new folders to put the relevant files into
os.makedirs(path + '/Tif/', exist_ok = True)
os.makedirs(path + '/LasLaz/', exist_ok = True)

#Move all of the relevant files into their folders
count = 0
for (dir_path, dir_names, file_names) in walk(path):
    for d in file_names:
        dir_path = dir_path.replace(os.sep, '/')
    
        fullPath = dir_path + '/' + d
        if fullPath[-4:] == '.tif':
            shutil.move(fullPath, path + '/Tif/' + d)
            count = count + 0.5
            
        if fullPath[-4:] == '.las':
            shutil.move(fullPath, path + '/LasLaz/' + d)
            count = count + 1
            
        if fullPath[-4:] == '.laz':
            shutil.move(fullPath, path + '/LasLaz/' + d)
            count = count + 1
            
#Delete the temp folders
shutil.rmtree(path + '/FilesExtract/')
shutil.rmtree(path + '/SubFiles/')

print ('Yeah done, successfully sorted ' + str(int(count)) + ' files')
