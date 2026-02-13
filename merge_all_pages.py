import os
from PyPDF2 import PdfMerger

folder_path = "pdf-data/TTD Darshan"
output_pdf = "merged_output.pdf"

merger = PdfMerger()

# Get all PDF files and sort them (important for sequence)
pdf_files = sorted(
    [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
)

for pdf in pdf_files:
    pdf_path = os.path.join(folder_path, pdf)
    merger.append(pdf_path)

# Write merged PDF
with open(output_pdf, "wb") as f:
    merger.write(f)

merger.close()

print("All PDFs merged successfully into", output_pdf)
