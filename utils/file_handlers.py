from typing import BinaryIO
import PyPDF2
import docx

def extract_text_from_pdf(file: BinaryIO) -> str:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_txt(file: BinaryIO) -> str:
    return file.read().decode('utf-8')

def extract_text_from_docx(file: BinaryIO) -> str:
    doc = docx.Document(file)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])
