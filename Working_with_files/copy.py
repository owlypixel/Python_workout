import shutil, os

MusicDir = r'C:\Users\aleskerov\Downloads\Music' # music source Directory
DestDir = 'E:\Podcast' # Destination directory

files = os.listdir(MusicDir)
no_files = True

for f in files:
    _, ext = os.path.splitext(f)
    if ext == '.mp3':
        if no_files:
            print('Found mp3 files - starting move procedure...')
        no_files = False
        shutil.move(MusicDir + '\\' + f, DestDir)
        print('File: ' + f + ' moved successfully!')

if no_files:
    print('No mp3 files found!')
else:
    print('All files moved successfully')
