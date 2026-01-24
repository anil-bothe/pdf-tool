import os
from PyPDF2 import PdfReader, PdfWriter

BASE_DIR = "pdf-data"
OUTPUT_FILE = "bulk.pdf"

writer = PdfWriter()
total_pages = 0

print("🚀 Starting bulk PDF creation...\n")

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if not file.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(root, file)
        print(f"➜ Processing: {pdf_path}")

        try:
            reader = PdfReader(pdf_path)
            if reader.pages:
                writer.add_page(reader.pages[0])
                total_pages += 1
                print("  ✅ Page added")
            else:
                print("  ⚠️ No pages found")

        except Exception as e:
            print(f"  ❌ Error: {e}")

with open(OUTPUT_FILE, "wb") as f:
    writer.write(f)

print(f"\n📝 Created bulk.pdf with {total_pages} pages")
print("✅ Bulk PDF creation completed.")
