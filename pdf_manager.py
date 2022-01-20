import os

from PyPDF2 import PdfFileReader


class PdfManager:

    def __init__(self) -> None:
        super().__init__()
        files = os.listdir(".prices")
        for file in files:
            with open(".prices/" + file, mode='rb') as f:
                reader = PdfFileReader(f)
                for page in reader.pages:
                    print(page.extractText())

            f.close()
