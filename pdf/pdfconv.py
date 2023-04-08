from PyPDF2 import PdfReader,PdfWriter,PdfFileWriter
import sys
#files =sys.argv[1:] #taking all arguments as a list
# pdf = PdfReader('twopage.pdf')
# number_of_pages = len(pdf.pages)
# page = pdf.pages[0]
# text = page.extract_text()
# print(text)
# print(".......................")
# print(f'number of pages is {number_of_pages}')

#######Merger###########
# merger=PdfWriter()
# for pdf in files:
#     merger.append(pdf)
# merger.write('mergedpdf.pdf')
# merger.close()
#### Adding Watermark to Pages ####
template = PdfReader('mergedpdf.pdf')
watermark = PdfReader('wtr.pdf')
op = PdfWriter()
for i in range(len(template.pages)):
    page= template.pages[i]
    page.merge_page(watermark.pages[0])
    op.add_page(page)

    with open('wmpdf.pdf','wb')as file:
        op.write(file)


