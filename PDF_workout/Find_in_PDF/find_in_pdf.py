import PyPDF2
import re

# open file in read binary mode
pdfFileObj = open('Folder_Tree.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pagesNum = pdfReader.numPages

# open file to write the file names
textFile = open('text.txt', 'w', encoding="utf-8")
for n in range (0, pagesNum):
	pageObj = pdfReader.getPage(n)
	text = pageObj.extractText()
	normalizedText = text.replace("\n", "")
	match = re.findall(r'(?:\w*)?\s\d.\d-(?:.[^|]*?)\.\w+', normalizedText)
	for i in match:
		textFile.write(i)
		textFile.write("\n")
textFile.close()

