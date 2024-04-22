import os
import json
import PyPDF2

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("error reading pdf file")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception(
            
            "unsupported file format"
        )