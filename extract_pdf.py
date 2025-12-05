import fitz # PyMuPDF

def extract_pdf_to_txt(pdf_path, txt_path):
    """
    Extracts all text from a PDF file and saves it to a TXT file.

    Args:
        pdf_path (str): The path to the input PDF file.
        txt_path (str): The path to the output TXT file.
    """
    try:
        with fitz.open(pdf_path) as doc:
            full_text = ""
            for page in doc:
                full_text += page.get_text()

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"Text successfully extracted from '{pdf_path}' to '{txt_path}'")
    except Exception as e:
        print(f"Error extracting text: {e}")

# Example usage:
pdf_file = "merged_document.pdf"  # Replace with your PDF file name
output_txt_file = "extracted_text.txt"

extract_pdf_to_txt(pdf_file, output_txt_file)