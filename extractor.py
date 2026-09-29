import os

def extract_text(filename):
    try:
        if filename.lower().endswith(".txt"):
            with open(filename, "r", encoding="utf-8") as file:
                return file.read()

        elif filename.lower().endswith(".pdf"):
            from pypdf import PdfReader

            reader = PdfReader(filename)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            if not text.strip():
                return "Error: No readable text found in the PDF."

            return text

        else:
            return "Error: Only PDF and TXT files are supported."

    except Exception as e:
        return f"Error: {str(e)}"