#!/usr/bin/env python3
import os
import PyPDF2
import re

def extract_text(pdf):
	text = ""
	pages = pdf.getNumPages()
	for page in range(pages):
		p = pdf.getPage(page)
		text += p.extractText() + "\n"
	text = re.sub(r'\n\s*\n', '\n', text)
	text = text.strip()
	return text

data_dir = "./data"
files = os.listdir(data_dir)
for file in files:
	filename = data_dir + "/" + file
	print(filename)
	f = open(filename, 'rb')
	try:
		pdf = PyPDF2.PdfFileReader(f)
		text = extract_text(pdf)
		print("Content length = " + str(len(text)))
		print(text)
	except Exception as e:
		print("Error reading " + filename + ": " + str(e))
	break