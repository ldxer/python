from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("cv.pdf", "rb"))

# print how many pages input1 has, because why not:
print ("Input has %d pages." % input1.getNumPages())
print("List the page numbers to delete. Sep. by spaces.")

old=' ';
count=0
for num in range(input1.numPages):
	texto = input1.getPage(num).extractText()
	new=texto
	if new !=old:
		output.addPage(input1.getPage(num))
		old=new
		count=count+1
	else:
		old=new
		
		
print ("Output has %d pages." % count)
outputStream = open("yPDF2-output.pdf", "wb")
output.write(outputStream)
