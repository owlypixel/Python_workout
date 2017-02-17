#! python3
import os

# printing a rawstring
print(r"C:\LAB\TEST")

# joining strings to create a file path
print('\\'.join(['folder1', 'folder2', 'folder3', 'folder4', 'folder5', 'file.png']))
print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

# getting current working directory
print(os.getcwd())

# setting current working directory
os.chdir('C:\\')
print(os.getcwd())

# getting an absolute path of the file
print(os.path.abspath('owl.png'))

# getting directory path
print(os.path.dirname('C:\LAB\TEST\owl.png'))

# getting the file name
print(os.path.basename('C:\LAB\TEST\owl.png'))

# check if file exists
print(os.path.exists('C:\LAB\TEST\owl.png'))

# check the file size
print(os.path.getsize(r'C:\LAB\Python_workout\Working_with_files\run.bat'))

# get a list of file names and folders in particular folder
print(os.listdir('C:\LAB\Python_workout\Working_with_files'))

# create a folder structure
print(os.makedirs('C:\LAB\Python_workout\Working_with_files\HOMO'))