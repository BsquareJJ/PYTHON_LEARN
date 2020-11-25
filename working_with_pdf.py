from PyPDF2 import PdfFileReader


with open('computer_science.pdf', 'rb') as pdf:
	readed_pdf = PdfFileReader(pdf)
	pdf_info = readed_pdf.getDocumentInfo()
	pages = readed_pdf.getNumPages()


print("[INFO]: THERE IS " + pages + " PAGES IN THIS DOCUMENT")
