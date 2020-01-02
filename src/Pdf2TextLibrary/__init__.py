from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


__version__ = '1.0.1'

class Pdf2TextLibrary(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self):
        self.codec = 'utf-8'
        self.password = ""
        self.maxpages = 0
        self.caching = True
        self.page_numbers = set()
        self.laparams = LAParams()
        self.resource_manager = PDFResourceManager()

    def convert_pdf_to_txt(self, file_path):
        string_io = StringIO()
        text_converter = TextConverter(
            self.resource_manager, string_io,
            codec=self.codec, laparams=self.laparams
        )
        page_interpreter = PDFPageInterpreter(self.resource_manager, text_converter)
        with open(file_path, 'rb') as file:
            pages = PDFPage.get_pages(
                file, self.page_numbers,
                maxpages=self.maxpages,
                password=self.password,
                caching=self.caching,
                check_extractable=True
            )
            for page in pages:
                page_interpreter.process_page(page)
        text_converter.close()
        result = string_io.getvalue()
        string_io.close()
        return result

    def count_pdf_pages(self, file_path):
        page_number = 0
        string_io = StringIO()
        text_converter = TextConverter(
            self.resource_manager, string_io,
            codec=self.codec, laparams=self.laparams
        )
        with open(file_path, 'rb') as file:
            pages = PDFPage.get_pages(
                file, self.page_numbers,
                maxpages=self.maxpages,
                password=self.password,
                caching=self.caching,
                check_extractable=True
            )
            for _ in enumerate(pages):
                page_number += 1
        text_converter.close()
        return page_number
