from cloud_assignment.skb_application.text_extraction.modules.text_extraction_functions import TextExtractionFunctions


class TextExtractor:
    def __init__(self, file_type):
        self.text_extraction_functions = TextExtractionFunctions()
        self.file_type = file_type

    def crop_pdf(self, file_path):
        return self.text_extraction_functions.crop_pdf(input_pdf_file_path=file_path)

    def extract_text(self, file_path):
        if self.file_type == "pdf":
            return self.text_extraction_functions.extract_text(file_path=file_path)

