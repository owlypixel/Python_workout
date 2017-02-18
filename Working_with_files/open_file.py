#! python3

# open file and read it and close
helloFile = open('Hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

# using readlines
helloFile = open('Hello.txt')
content_as_list = helloFile.readlines()
print(content_as_list)
helloFile.close()