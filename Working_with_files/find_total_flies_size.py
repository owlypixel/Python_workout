#! python3
import os

# a small program that calculates total size of the files in a given directory

totalSize = 0
searchDirectory = 'C:\LAB\Python_workout\Working_with_files'
allFiles = os.listdir(searchDirectory)
print(allFiles)

for filename in allFiles:
	if not os.path.isfile(searchDirectory + os.path.sep + filename):
		continue
	totalSize += os.path.getsize(searchDirectory + os.path.sep + filename)

print(totalSize)

