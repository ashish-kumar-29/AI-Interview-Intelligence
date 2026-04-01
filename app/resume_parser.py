import pdfplumber
from docx import Document
import io


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text


def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def parse_resume(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file.file)

    elif filename.endswith(".docx"):
        file_content = io.BytesIO(file.file.read())
        return extract_text_from_docx(file_content)

    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")