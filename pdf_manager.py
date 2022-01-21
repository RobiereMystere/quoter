import math
import os
import pdfplumber
from pdfplumber.table import DEFAULT_MIN_WORDS_VERTICAL


class PdfManager:

    def __init__(self) -> None:
        super().__init__()
        files = os.listdir(".prices")
        for file in files:
            with pdfplumber.open(".prices/" + file) as pdf:
                page = pdf.pages[0]
                # for page in pdf.pages:

                # print(page.images)
                # print(page.rects)
                dict_char = page.chars
                y0 = 0
                x1 = 0
                for t in dict_char:
                    if y0 != t['y0']:
                        print()
                        y0 = t['y0']
                    if math.fabs(t['x1'] - x1) > 10:
                        #print(math.fabs(t['x1'] - x1))
                        print(" ", end='')
                    print(t['text'], end='')
                    x1 = t['x1']
                    """for lines in page.extract_tables({'horizontal_strategy': "text"}):
                        for cells in lines:
                            for cell in cells:
                                if cell is not None:
                                    print(cell)"""
