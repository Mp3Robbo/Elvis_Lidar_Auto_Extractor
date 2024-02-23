Elvis (Elevation and Depth - Foundation Spatial Data) is a great website for getting spatial data

However having to deal with files inside zip folders inside zip folders can get quite tedious

___________________

Run this python file in the same directory as the zip folder and it will unzip and sort the files into two folders: tif and las/laz

The way to run it through cmd would be something like

cd C:/FolderWithTheFiles/

python Elvis_Lidar_Auto_Extractor.py

_______________________

I think that there may be some issues when some files are two zips deep, while others only one, so let me know if anything like this comes up

Also this script could be improved so that it sorts more than just the two file types, so if you have any improvements put them in the discussion
