#! python3
# -*- coding: utf-8 -*-
import sys
import PyPDF2
import os

print (sys.stdout.encoding)

pdfFile = open('weekender.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())
