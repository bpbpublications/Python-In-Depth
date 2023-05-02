
import PyPDF2

with open("./testing_files/sample.pdf", 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    count = pdf_reader.numPages

    for i in range(count):
        page = pdf_reader.getPage(i)
        page_text = page.extractText()
        print(page_text)
