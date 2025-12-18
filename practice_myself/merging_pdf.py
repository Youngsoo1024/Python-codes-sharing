from pypdf import PdfWriter
import os

    # Create a PdfMerger object
merger = PdfWriter()

    # Define the directory containing your PDF files
pdf_directory = "pdf" 

    # Iterate through PDF files in the directory and append them
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_directory, filename)
        merger.append(filepath)

    # Write the merged PDF to a new file
output_filename = "merged_document.pdf"
merger.write(output_filename)

    # Close the merger object
merger.close()

print(f"PDFs merged successfully into {output_filename}")