from PyPDF2 import PdfWriter, PdfReader
import pdfplumber


class TextExtractionFunctions:
    def __init__(self):
        self.pdf_title = None

    def crop_pdf(self, input_pdf_file_path):
        with open(input_pdf_file_path, "rb") as in_f:
            input1 = PdfReader(in_f)
            output = PdfWriter()

            numPages = len(input1.pages)
            print("document has %s pages." % numPages)

            for i in range(numPages):
                page = input1.pages[i]
                if (page.mediabox.width < 595) and (page.mediabox.height < 842):
                    page.cropbox.lower_left = (50, 75)
                    page.cropbox.upper_right = (600, 800)
                    output.add_page(page)
                else:
                    page.cropbox.lower_left = (30, 95)
                    page.cropbox.upper_right = (1000, 530)
                    output.add_page(page)
            with open("./pdf_files/cropped_pdf.pdf", "wb") as out_f:
                output.write(out_f)
        return

    def extract_text(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            extracted_lines = []
            for page in pdf.pages:
                extracted_text = page.extract_text()
                lines = extracted_text.strip().split("\n")
                lines.pop(-2)
                extracted_lines.extend(lines)
        return extracted_lines