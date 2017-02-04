#! python3
# -*- coding: utf-8 -*-
import sys
import PyPDF2
import os

print (sys.stdout.encoding)

pdf1File = open('weekender.pdf', 'rb')
pdf2File = open('bluesXP.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

outputFile = open('combined_doc.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()