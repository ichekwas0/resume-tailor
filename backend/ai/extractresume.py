from PyPDF2 import PdfReader

def extract(resume_url):
    resume_str = ""
    reader = PdfReader(resume_url)
    pages = reader.pages
    for i in range(len(pages)):
        text = pages[i].extract_text()
        if text:
            resume_str += text
    return resume_str
        