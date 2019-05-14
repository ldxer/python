from PyPDF2 import PdfFileReader,PdfFileWriter
from PyPDF2.pdf import PageObject

import  time
import sys
writer=PdfFileWriter()
pdf_input=sys.argv[1]
pdf_in=PdfFileReader(open(pdf_input,"rb"))
num=pdf_in.getNumPages()
for i in range(0,num,1):
	sup_page=pdf_in.getPage(i)
	translated_page = PageObject.createBlankPage(None, sup_page.mediaBox.getWidth()+500, sup_page.mediaBox.getHeight()+50)
	#translated_page=pdf_in2.getPage(i)
	translated_page.mergeTranslatedPage(sup_page,250,0)
	writer.addPage(translated_page)
	
	

with open("final.pdf","wb") as outfb:
    writer.write(outfb)
outfb.close()

