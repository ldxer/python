from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("obj2.pdf", "rb"))

# print how many pages input1 has, because why not:
print("Input has %d pages." % input1.getNumPages())

for num in range(32,36):
     output.addPage(input1.getPage(num))

outputStream = open("Objective_Union_and_its_Territories.pdf", "wb")
output.write(outputStream)


