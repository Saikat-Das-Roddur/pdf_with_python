import PyPDF2
import sys

# inputs = sys.argv[1:]

# obj = open('dummy.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(obj)
# page  = pdfReader.getPage(0)
# print(page.rotateCounterClockwise(90))
# writer = PyPDF2.PdfFileWriter()
# writer.addPage(page)
# pdf = open('tilt.pdf', 'wb')
# writer.write(pdf)

# merger code

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('supper.pdf')
# pdf_combiner(inputs)

# adding watermark
template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    output.write(open('water_marked.pdf','wb'))
