from PyPDF2 import PdfReader
import pdfplumber
import pandas as pd



#Try PyPDF2 first
def nice(pdf_path):
        reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        

        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            
        with open("text.txt","w") as f:
            f.write(text)

        return True
            


