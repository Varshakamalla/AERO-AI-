import os
import fitz  # PyMuPDF
import json

def extract_pdfs():
    pdf_folder = "chatbot/knowledge/pdfs"
    output = []

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_folder, filename)
            doc = fitz.open(path)
            text = ""
            for page in doc:
                text += page.get_text()
            output.append({
                "title": filename,
                "content": text.replace("\n", " ").strip()
            })

    with open("chatbot/knowledge/documents.json", "a", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"✅ Extracted text from {len(output)} PDFs.")

if __name__ == "__main__":
    extract_pdfs()
